const TARGETS = [
  "Visual & Temporal Quality",
  "Spatial & State Consistency",
  "Long-Horizon Memory & State Persistence",
  "Physical Plausibility",
  "Causal & Counterfactual Reasoning",
  "Control Fidelity & Interactive Dynamics",
  "Functional Utility",
];
const PROTOCOLS = ["OL", "CR", "CL"];
const METRICS = ["A", "J", "O"];
const EVALUATION_DATA = ["RWD", "SBG", "SPTC", "HCP"];
const TARGET_COLORS = {
  "Visual & Temporal Quality": "#6f63d9",
  "Spatial & State Consistency": "#2f88b7",
  "Long-Horizon Memory & State Persistence": "#4d998f",
  "Physical Plausibility": "#d05f68",
  "Causal & Counterfactual Reasoning": "#c25b87",
  "Control Fidelity & Interactive Dynamics": "#d5783b",
  "Functional Utility": "#45a15a",
};

// The first project-page release used the preceding three-dimensional draft.
// These rules migrate its static shards to the latest four-dimensional PDF
// (Target–Protocol–Metrics–Data) without duplicating the 84-record corpus.
const LEGACY_DATA_CODE_MAP = { RO: "RWD", SG: "SBG", CSI: "SPTC", HRS: "HCP" };
const LATEST_DATA_OVERRIDES = new Map([
  [34, ["HCP"]], // 4DWorldBench
  [39, ["HCP"]], // TC-Bench
  [73, ["HCP"]], // CRONOS
  [75, ["HCP"]], // PhysicsMind
  [81, ["HCP"]], // MMWorld
  [91, ["HCP"]], // Omni-WorldBench
  [92, ["HCP"]], // WorldSimBench
]);
const REMOVE_REAL_WORLD_DAGGER = new Set([24, 95]);

const state = {
  benchmarks: [],
  metadata: null,
  search: "",
  sort: "recent",
  year: null,
  filters: {
    targets: new Set(),
    protocols: new Set(),
    metrics: new Set(),
    domains: new Set(),
    evaluationData: new Set(),
  },
};

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const els = {
  grid: $("#benchmark-grid"),
  search: $("#benchmark-search"),
  searchClear: $("#search-clear"),
  sort: $("#benchmark-sort"),
  resultCount: $("#result-count"),
  empty: $("#empty-state"),
  emptyClear: $("#empty-clear"),
  activeFilters: $("#active-filters"),
  clearFilters: $("#clear-filters"),
  filterLabel: $("#filter-count-label"),
  openFilters: $("#open-filters"),
  closeFilters: $("#close-filters"),
  filterBackdrop: $("#filter-backdrop"),
  mobileFilterCount: $("#mobile-filter-count"),
  targetShortcuts: $("#target-shortcuts"),
  protocolShortcuts: $("#protocol-shortcuts"),
  metricsShortcuts: $("#metrics-shortcuts"),
  dataShortcuts: $("#data-shortcuts"),
  matrix: $("#taxonomy-matrix"),
  timeline: $("#timeline-chart"),
  clearYear: $("#clear-year"),
  copyCitation: $("#copy-citation"),
  citation: $("#citation-code"),
  downloadJson: $("#download-json"),
};

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function normalizeLatestRecord(item) {
  const mappedData = (item.evaluationData || item.dataConstruction || [])
    .map((code) => LEGACY_DATA_CODE_MAP[code] || code);
  const evaluationData = LATEST_DATA_OVERRIDES.get(Number(item.ref)) || [...new Set(mappedData)];
  return {
    ...item,
    metrics: [...(item.metrics || item.evidence || [])],
    evaluationData,
    realWorldExecution: REMOVE_REAL_WORLD_DAGGER.has(Number(item.ref)) ? false : Boolean(item.realWorldExecution),
  };
}

function prettyDomain(value) {
  const labels = { video: "Video", embodied: "Embodied", driving: "Driving", game: "Game" };
  return labels[value] || value.replace(/\b\w/g, (character) => character.toUpperCase());
}

function groupLabel(group, value) {
  if (group === "protocols") return state.metadata.protocolLabels[value] || value;
  if (group === "metrics") return state.metadata.metricLabels[value] || value;
  if (group === "evaluationData") return state.metadata.dataLabels[value] || value;
  if (group === "domains") return prettyDomain(value);
  return value;
}

function normalizedSearchText(item) {
  return [
    item.shortName,
    item.title,
    item.venue,
    item.domains.join(" "),
    item.targets.join(" "),
    item.subtargets.join(" "),
    item.protocols.join(" "),
    item.metrics.join(" "),
    item.evaluationData.join(" "),
    item.reference,
  ].join(" ").toLowerCase();
}

function matchesSearch(item) {
  if (!state.search) return true;
  const terms = state.search.toLowerCase().trim().split(/\s+/).filter(Boolean);
  const haystack = normalizedSearchText(item);
  return terms.every((term) => haystack.includes(term));
}

function matchesGroup(item, group, ignoredGroup = null) {
  if (group === ignoredGroup) return true;
  const active = state.filters[group];
  if (!active.size) return true;
  return item[group].some((value) => active.has(value));
}

function matchesItem(item, ignoredGroup = null) {
  if (!matchesSearch(item)) return false;
  if (state.year && item.year !== state.year) return false;
  return Object.keys(state.filters).every((group) => matchesGroup(item, group, ignoredGroup));
}

function visibleItems() {
  const items = state.benchmarks.filter((item) => matchesItem(item));
  if (state.sort === "oldest") {
    items.sort((a, b) => a.year - b.year || a.shortName.localeCompare(b.shortName));
  } else if (state.sort === "title") {
    items.sort((a, b) => a.shortName.localeCompare(b.shortName));
  } else {
    items.sort((a, b) => b.year - a.year || a.shortName.localeCompare(b.shortName));
  }
  return items;
}

function countForValue(group, value) {
  return state.benchmarks.filter((item) => {
    if (!matchesSearch(item)) return false;
    if (state.year && item.year !== state.year) return false;
    if (!Object.keys(state.filters).every((key) => matchesGroup(item, key, group))) return false;
    return item[group].includes(value);
  }).length;
}

function uniqueValues(group) {
  if (group === "targets") return TARGETS;
  if (group === "protocols") return PROTOCOLS;
  if (group === "metrics") return METRICS;
  if (group === "evaluationData") return EVALUATION_DATA;
  return [...new Set(state.benchmarks.flatMap((item) => item[group]))]
    .sort((a, b) => groupLabel(group, a).localeCompare(groupLabel(group, b)));
}

function activeFilterCount() {
  return Object.values(state.filters).reduce((sum, set) => sum + set.size, 0) + (state.year ? 1 : 0);
}

function toggleFilter(group, value, force = null) {
  const set = state.filters[group];
  const shouldAdd = force == null ? !set.has(value) : force;
  if (shouldAdd) set.add(value);
  else set.delete(value);
  updateUrl();
  renderAll();
}

function setFocusedFilters(target = null, protocol = null) {
  Object.values(state.filters).forEach((set) => set.clear());
  state.year = null;
  if (target) state.filters.targets.add(target);
  if (protocol) state.filters.protocols.add(protocol);
  updateUrl();
  renderAll();
  document.querySelector("#benchmarks").scrollIntoView({ behavior: "smooth", block: "start" });
}

function clearAll() {
  state.search = "";
  state.year = null;
  Object.values(state.filters).forEach((set) => set.clear());
  els.search.value = "";
  els.searchClear.hidden = true;
  updateUrl();
  renderAll();
}

function buildFilters() {
  Object.keys(state.filters).forEach((group) => {
    const container = document.querySelector(`[data-filter-group="${group}"]`);
    container.innerHTML = "";
    uniqueValues(group).forEach((value) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "filter-option";
      button.dataset.group = group;
      button.dataset.value = value;
      button.setAttribute("aria-pressed", "false");
      button.innerHTML = `<span class="filter-check" aria-hidden="true"></span><span class="filter-text">${escapeHtml(groupLabel(group, value))}</span><span class="filter-number">0</span>`;
      button.addEventListener("click", () => toggleFilter(group, value));
      container.append(button);
    });
  });
}

function updateFilters() {
  Object.keys(state.filters).forEach((group) => {
    const container = document.querySelector(`[data-filter-group="${group}"]`);
    $$(".filter-option", container).forEach((button) => {
      const value = button.dataset.value;
      const count = countForValue(group, value);
      const active = state.filters[group].has(value);
      button.setAttribute("aria-pressed", String(active));
      $(".filter-number", button).textContent = count;
      button.disabled = count === 0 && !active;
    });
  });
  const count = activeFilterCount();
  els.mobileFilterCount.textContent = count;
  els.filterLabel.textContent = count ? `${count} active filter${count === 1 ? "" : "s"}` : "All benchmarks";
}

function addActiveChip(prefix, label, onClick) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "active-chip";
  button.innerHTML = `${prefix ? `<b>${escapeHtml(prefix)}:</b> ` : ""}${escapeHtml(label)} <span aria-hidden="true">×</span>`;
  button.addEventListener("click", onClick);
  els.activeFilters.append(button);
}

function renderActiveFilters() {
  els.activeFilters.innerHTML = "";
  if (state.search) addActiveChip("Search", state.search, () => {
    state.search = "";
    els.search.value = "";
    els.searchClear.hidden = true;
    updateUrl();
    renderAll();
  });
  if (state.year) addActiveChip("Year", state.year, () => {
    state.year = null;
    updateUrl();
    renderAll();
  });
  Object.entries(state.filters).forEach(([group, set]) => {
    [...set].forEach((value) => addActiveChip(null, groupLabel(group, value), () => toggleFilter(group, value, false)));
  });
}

function targetShortLabel(target) {
  const labels = {
    "Visual & Temporal Quality": "Visual & Temporal Quality",
    "Spatial & State Consistency": "Spatial & State Consistency",
    "Long-Horizon Memory & State Persistence": "Long-Horizon Memory & Persistence",
    "Physical Plausibility": "Physical Plausibility",
    "Causal & Counterfactual Reasoning": "Causal & Counterfactual Reasoning",
    "Control Fidelity & Interactive Dynamics": "Control Fidelity & Interactive Dynamics",
    "Functional Utility": "Functional Utility",
  };
  return labels[target] || target;
}

function buildShortcuts() {
  const groups = [
    [els.targetShortcuts, TARGETS, "targets"],
    [els.protocolShortcuts, PROTOCOLS, "protocols"],
    [els.metricsShortcuts, METRICS, "metrics"],
    [els.dataShortcuts, EVALUATION_DATA, "evaluationData"],
  ];
  groups.forEach(([container, values, group]) => {
    container.innerHTML = "";
    values.forEach((value, index) => {
      const count = state.benchmarks.filter((item) => item[group].includes(value)).length;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "taxonomy-option";
      const label = group === "targets" ? targetShortLabel(value) : groupLabel(group, value);
      button.innerHTML = `<span>${group === "targets" ? `${index + 1}. ` : ""}${escapeHtml(label)}</span><span>${count}</span>`;
      button.addEventListener("click", () => {
        Object.values(state.filters).forEach((set) => set.clear());
        state.year = null;
        state.filters[group].add(value);
        updateUrl();
        renderAll();
        document.querySelector("#benchmarks").scrollIntoView({ behavior: "smooth" });
      });
      container.append(button);
    });
  });
}

function createMatrixHead(text) {
  const head = document.createElement("div");
  head.className = "matrix-head";
  head.textContent = text;
  return head;
}

function buildMatrix() {
  els.matrix.innerHTML = "";
  els.matrix.append(createMatrixHead("Evaluation target"));
  PROTOCOLS.forEach((protocol) => els.matrix.append(createMatrixHead(state.metadata.protocolLabels[protocol])));
  const allCounts = [];
  TARGETS.forEach((target) => PROTOCOLS.forEach((protocol) => {
    allCounts.push(state.benchmarks.filter((item) => item.targets.includes(target) && item.protocols.includes(protocol)).length);
  }));
  const max = Math.max(...allCounts, 1);
  TARGETS.forEach((target) => {
    const label = document.createElement("div");
    label.className = "matrix-row-label";
    label.textContent = targetShortLabel(target);
    els.matrix.append(label);
    PROTOCOLS.forEach((protocol) => {
      const count = state.benchmarks.filter((item) => item.targets.includes(target) && item.protocols.includes(protocol)).length;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "matrix-cell";
      button.style.setProperty("--heat", Math.round((count / max) * 100));
      button.setAttribute("aria-label", `${target}, ${state.metadata.protocolLabels[protocol]}: ${count} benchmarks`);
      button.innerHTML = `<strong>${count}</strong><small>benchmarks</small>`;
      button.addEventListener("click", () => setFocusedFilters(target, protocol));
      els.matrix.append(button);
    });
  });
}

function buildTimeline() {
  els.timeline.innerHTML = "";
  const years = [];
  for (let year = state.metadata.yearMin; year <= state.metadata.yearMax; year += 1) years.push(year);
  const counts = years.map((year) => state.benchmarks.filter((item) => item.year === year).length);
  const max = Math.max(...counts, 1);
  let cumulative = 0;
  years.forEach((year, index) => {
    cumulative += counts[index];
    const column = document.createElement("div");
    column.className = "year-column";
    const area = document.createElement("div");
    area.className = "year-bar-area";
    const bar = document.createElement("button");
    bar.type = "button";
    bar.className = "year-bar";
    bar.style.setProperty("--height", Math.max(5, Math.round((counts[index] / max) * 100)));
    bar.setAttribute("aria-pressed", String(state.year === year));
    bar.setAttribute("aria-label", `${year}: ${counts[index]} new benchmarks, ${cumulative} cumulative`);
    bar.innerHTML = `<span class="year-count">${counts[index]}</span>`;
    bar.addEventListener("click", () => {
      state.year = state.year === year ? null : year;
      updateUrl();
      renderAll();
      document.querySelector("#benchmarks").scrollIntoView({ behavior: "smooth" });
    });
    area.append(bar);
    const label = document.createElement("div");
    label.className = "year-label";
    label.innerHTML = `<strong>${year}</strong><small>${cumulative} cumulative</small>`;
    column.append(area, label);
    els.timeline.append(column);
  });
  els.clearYear.hidden = !state.year;
}

function protocolText(item) {
  return item.protocols.join(" · ");
}

function renderCards(items) {
  els.grid.innerHTML = "";
  items.forEach((item) => {
    const card = document.createElement("article");
    card.className = "benchmark-card";
    card.style.setProperty("--card-accent", TARGET_COLORS[item.targets[0]] || "#6f63d9");
    const targetPills = item.targets.map((target) => `<span class="target-pill">${escapeHtml(targetShortLabel(target))}</span>`).join("");
    const subtarget = item.subtargets.length ? item.subtargets.join(" · ") : "Paper taxonomy snapshot";
    card.innerHTML = `
      <div class="card-topline">
        <span class="card-year">${item.year} · ${escapeHtml(item.venue)}</span>
        ${item.crossCategory ? '<span class="cross-badge">△ Cross-category</span>' : ""}
      </div>
      <h3>${escapeHtml(item.shortName)}</h3>
      <p class="paper-title">${escapeHtml(item.title.replace(/[,.]+$/, ""))}</p>
      <div class="card-meta">
        <span class="meta-pill">${item.domains.map(prettyDomain).join(" + ")}</span>
        <span class="meta-pill">Protocol ${escapeHtml(protocolText(item))}</span>
        <span class="meta-pill">Metrics ${escapeHtml(item.metrics.join(" · "))}</span>
        <span class="meta-pill">Data ${escapeHtml(item.evaluationData.join(" · "))}</span>
      </div>
      <div class="card-targets">${targetPills}</div>
      <div class="card-footer">
        <small>Ref. [${item.ref}] · ${escapeHtml(subtarget)}</small>
        <a class="paper-link" href="${escapeHtml(item.paperUrl)}" target="_blank" rel="noreferrer">${item.arxivId ? "Paper" : "Scholar"} <span aria-hidden="true">↗</span></a>
      </div>`;
    els.grid.append(card);
  });
}

function renderAll() {
  const items = visibleItems();
  els.resultCount.textContent = items.length;
  $("#stat-total").textContent = state.metadata.total;
  els.empty.hidden = items.length !== 0;
  els.grid.hidden = items.length === 0;
  renderCards(items);
  updateFilters();
  renderActiveFilters();
  buildTimeline();
}

function openFilters() {
  document.body.classList.add("filters-open");
  els.filterBackdrop.hidden = false;
  setTimeout(() => els.closeFilters.focus(), 50);
}

function closeFilters() {
  document.body.classList.remove("filters-open");
  els.filterBackdrop.hidden = true;
}

function updateUrl() {
  const params = new URLSearchParams();
  if (state.search) params.set("q", state.search);
  if (state.year) params.set("year", state.year);
  const keys = { targets: "target", protocols: "protocol", metrics: "metrics", domains: "domain", evaluationData: "data" };
  Object.entries(keys).forEach(([group, key]) => {
    if (state.filters[group].size) params.set(key, [...state.filters[group]].join("|"));
  });
  const query = params.toString();
  try {
    history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
  } catch {
    // Filtering still works when URL state cannot be written in a local preview.
  }
}

function readUrl() {
  const params = new URLSearchParams(location.search);
  state.search = params.get("q") || "";
  const year = Number(params.get("year"));
  state.year = Number.isFinite(year) && year ? year : null;
  const keys = { targets: "target", protocols: "protocol", metrics: "metrics", domains: "domain", evaluationData: "data" };
  Object.entries(keys).forEach(([group, key]) => {
    const value = params.get(key) || (group === "metrics" ? params.get("evidence") : null);
    if (value) value.split("|").filter(Boolean).forEach((part) => state.filters[group].add(part));
  });
  els.search.value = state.search;
  els.searchClear.hidden = !state.search;
}

function alignedExport() {
  return {
    title: state.metadata.title,
    version: state.metadata.version,
    framework: state.metadata.framework,
    total: state.metadata.total,
    crossCategory: state.metadata.crossCategory,
    protocolLabels: state.metadata.protocolLabels,
    metricLabels: state.metadata.metricLabels,
    dataLabels: state.metadata.dataLabels,
    benchmarks: state.benchmarks.map((item) => ({
      id: item.id,
      shortName: item.shortName,
      title: item.title,
      ref: item.ref,
      year: item.year,
      venue: item.venue,
      domains: item.domains,
      protocols: item.protocols,
      metrics: item.metrics,
      evaluationData: item.evaluationData,
      targets: item.targets,
      subtargets: item.subtargets,
      crossCategory: item.crossCategory,
      paperUrl: item.paperUrl,
      arxivId: item.arxivId,
      reference: item.reference,
    })),
  };
}

function downloadAlignedJson() {
  const payload = JSON.stringify(alignedExport(), null, 2);
  const blob = new Blob([payload], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = "world-model-evaluation-benchmarks-july-2026.json";
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
}

function setupEvents() {
  let searchTimer = null;
  els.search.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      state.search = els.search.value.trim();
      els.searchClear.hidden = !state.search;
      updateUrl();
      renderAll();
    }, 120);
  });
  els.searchClear.addEventListener("click", () => {
    state.search = "";
    els.search.value = "";
    els.searchClear.hidden = true;
    updateUrl();
    renderAll();
    els.search.focus();
  });
  els.sort.addEventListener("change", () => {
    state.sort = els.sort.value;
    renderAll();
  });
  els.clearFilters.addEventListener("click", clearAll);
  els.emptyClear.addEventListener("click", clearAll);
  els.openFilters.addEventListener("click", openFilters);
  els.closeFilters.addEventListener("click", closeFilters);
  els.filterBackdrop.addEventListener("click", closeFilters);
  els.clearYear.addEventListener("click", () => {
    state.year = null;
    updateUrl();
    renderAll();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && document.body.classList.contains("filters-open")) closeFilters();
  });
  $$(".taxonomy-jump").forEach((button) => {
    button.addEventListener("click", () => document.getElementById(button.dataset.scrollTarget)?.scrollIntoView({ behavior: "smooth", block: "center" }));
  });
  els.copyCitation.addEventListener("click", async () => {
    const text = els.citation.innerText;
    try {
      await navigator.clipboard.writeText(text);
      const previous = els.copyCitation.textContent;
      els.copyCitation.textContent = "Copied";
      setTimeout(() => { els.copyCitation.textContent = previous; }, 1400);
    } catch {
      window.prompt("Copy this BibTeX:", text);
    }
  });
  els.downloadJson.addEventListener("click", downloadAlignedJson);
}

function setupNavObserver() {
  const links = $$(".primary-nav a");
  const sections = links.map((link) => document.querySelector(link.getAttribute("href"))).filter(Boolean);
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    links.forEach((link) => link.removeAttribute("aria-current"));
    const active = links.find((link) => link.getAttribute("href") === `#${visible.target.id}`);
    if (active) active.setAttribute("aria-current", "true");
  }, { rootMargin: "-25% 0px -65%", threshold: [0, 0.15, 0.4] });
  sections.forEach((section) => observer.observe(section));
}

async function init() {
  try {
    const dataFiles = [1, 2, 3, 4].map((index) => `assets/benchmarks-${index}.json`);
    const responses = await Promise.all([...dataFiles, "assets/metadata.json"].map((url) => fetch(url)));
    const failed = responses.find((response) => !response.ok);
    if (failed) throw new Error(`HTTP ${failed.status}`);
    const decoded = await Promise.all(responses.map((response) => response.json()));
    state.benchmarks = decoded.slice(0, 4).flat().map(normalizeLatestRecord);
    state.metadata = decoded[4];
    if (state.benchmarks.length !== state.metadata.total) {
      throw new Error(`Expected ${state.metadata.total} benchmarks, loaded ${state.benchmarks.length}`);
    }
    readUrl();
    buildFilters();
    buildShortcuts();
    buildMatrix();
    setupEvents();
    setupNavObserver();
    renderAll();
  } catch (error) {
    console.error(error);
    els.grid.innerHTML = `<div class="empty-state"><h3>Benchmark data could not be loaded.</h3><p>${escapeHtml(error.message)}</p></div>`;
  }
}

init();
