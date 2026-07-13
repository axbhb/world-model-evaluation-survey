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

function addActiveChip(prefix, label, onClick) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "active-chip";
  button.innerHTML = `${prefix ? `<b>${escapeHtml(prefix)}:</b> ` : ""}${escapeHtml(label)} <span aria-hidden="true">×</span>`;
  button.addEventListener("click", onClick);
  els.activeFilters.append(button);
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
    [els.evidenceShortcuts, EVIDENCE, "evidence"],
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

function createMatrixHead(text) {
  const head = document.createElement("div");
  head.className = "matrix-head";
  head.textContent = text;
  return head;
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
    const col = document.createElement("div");
    col.className = "year-column";
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
    col.append(area, label);
    els.timeline.append(col);
  });
  els.clearYear.hidden = !state.year;
}

function protocolText(item) {
  const labels = item.protocols.map((key) => key + (item.realWorldExecution && key === "CL" ? "†" : ""));
  return labels.join(" · ");
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
        <span class="meta-pill">Evidence ${escapeHtml(item.evidence.join(" · "))}</span>
        <span class="meta-pill">Data ${escapeHtml(item.dataConstruction.join(" · "))}</span>
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
  const keys = { targets: "target", protocols: "protocol", evidence: "evidence", domains: "domain", dataConstruction: "data" };
  Object.entries(keys).forEach(([group, key]) => {
    if (state.filters[group].size) params.set(key, [...state.filters[group]].join("|"));
  });
  const query = params.toString();
  try {
    history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
  } catch {
    // Some local preview contexts use an opaque origin; filtering still works without URL sync.
  }
}

function readUrl() {
  const params = new URLSearchParams(location.search);
  state.search = params.get("q") || "";
  const year = Number(params.get("year"));
  state.year = Number.isFinite(year) && year ? year : null;
  const keys = { targets: "target", protocols: "protocol", evidence: "evidence", domains: "domain", dataConstruction: "data" };
  Object.entries(keys).forEach(([group, key]) => {
    const value = params.get(key);
    if (value) value.split("|").filter(Boolean).forEach((part) => state.filters[group].add(part));
  });
  els.search.value = state.search;
  els.searchClear.hidden = !state.search;
}

