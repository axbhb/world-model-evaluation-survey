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
const EVIDENCE = ["A", "J", "O"];
const TARGET_COLORS = {
  "Visual & Temporal Quality": "#6f63d9",
  "Spatial & State Consistency": "#2f88b7",
  "Long-Horizon Memory & State Persistence": "#4d998f",
  "Physical Plausibility": "#d05f68",
  "Causal & Counterfactual Reasoning": "#c25b87",
  "Control Fidelity & Interactive Dynamics": "#d5783b",
  "Functional Utility": "#45a15a",
};

const state = {
  benchmarks: [],
  metadata: null,
  search: "",
  sort: "recent",
  year: null,
  filters: {
    targets: new Set(),
    protocols: new Set(),
    evidence: new Set(),
    domains: new Set(),
    dataConstruction: new Set(),
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
  evidenceShortcuts: $("#evidence-shortcuts"),
  matrix: $("#taxonomy-matrix"),
  timeline: $("#timeline-chart"),
  clearYear: $("#clear-year"),
  copyCitation: $("#copy-citation"),
  citation: $("#citation-code"),
};

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function prettyDomain(value) {
  const labels = { video: "Video", embodied: "Embodied", driving: "Driving", game: "Game" };
  return labels[value] || value.replace(/\b\w/g, (c) => c.toUpperCase());
}

function groupLabel(group, value) {
  if (group === "protocols") return state.metadata.protocolLabels[value] || value;
  if (group === "evidence") return state.metadata.evidenceLabels[value] || value;
  if (group === "dataConstruction") return state.metadata.dataLabels[value] || value;
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
    item.evidence.join(" "),
    item.dataConstruction.join(" "),
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
  if (group === "evidence") return EVIDENCE;
  return [...new Set(state.benchmarks.flatMap((item) => item[group]))].sort((a, b) => groupLabel(group, a).localeCompare(groupLabel(group, b)));
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

