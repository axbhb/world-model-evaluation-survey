(() => {
  const LABELS = {
    protocol: {
      OL: "Open-Loop Prediction",
      CR: "Controlled Rollout",
      CL: "Closed-Loop Interaction",
    },
    metrics: {
      A: "Automatic Metrics",
      J: "Judge-Based Metrics",
      O: "Outcome-Grounded Metrics",
    },
    data: {
      RWD: "Real-World Data Collection",
      SBG: "Simulation-Based Generation",
      SPTC: "Scenario, Prompt, and Task Curation",
      HCP: "Hybrid Construction Pipelines",
    },
  };

  function expandCodes(text, prefix, labels) {
    const raw = String(text || "").replace(new RegExp(`^${prefix}\\s*:?\\s*`, "i"), "").trim();
    const expanded = raw
      .split(/\s*[·+]\s*/)
      .filter(Boolean)
      .map((code) => labels[code] || code)
      .join(" · ");
    return expanded ? `${prefix}: ${expanded}` : prefix;
  }

  function setTextIfChanged(element, nextText) {
    if (element && element.textContent !== nextText) element.textContent = nextText;
  }

  function installTimelineAnalysis() {
    const shell = document.querySelector(".timeline-shell");
    if (!shell || shell.querySelector(".timeline-analysis")) return;

    const toolbar = shell.querySelector(".timeline-toolbar");
    const chart = shell.querySelector(".timeline-chart");
    if (!toolbar || !chart) return;

    const main = document.createElement("div");
    main.className = "timeline-main";
    shell.insertBefore(main, toolbar);
    main.append(toolbar, chart);

    const analysis = document.createElement("aside");
    analysis.className = "timeline-analysis";
    analysis.setAttribute("aria-labelledby", "timeline-analysis-title");
    analysis.innerHTML = `
      <p class="timeline-analysis-kicker">Growth analysis</p>
      <h3 id="timeline-analysis-title">Benchmark growth accelerated—and evaluation targets broadened.</h3>
      <div class="timeline-analysis-stats" aria-label="Key benchmark growth statistics">
        <div class="timeline-analysis-stat"><strong>17.1%</strong><span>introduced before 2024</span></div>
        <div class="timeline-analysis-stat"><strong>2.4×</strong><span>increase from 2024 to 2025</span></div>
        <div class="timeline-analysis-stat"><strong>68.3%</strong><span>introduced in 2025–2026</span></div>
        <div class="timeline-analysis-stat"><strong>39</strong><span>Physical Plausibility benchmarks</span></div>
      </div>
      <div class="timeline-analysis-copy">
        <p>Figure 2 reveals a shift not only in the volume of world-model benchmarks but also in the composition of their evaluation targets. Only <strong>14 of the 82 benchmarks (17.1%)</strong> were introduced before 2024, with early efforts concentrated primarily on visual and temporal quality, controlled physical reasoning, and causal understanding.</p>
        <p>The number of newly introduced benchmarks then increased from <strong>12 in 2024 to 29 in 2025</strong>, representing a <strong>2.4-fold increase</strong> and raising the cumulative total from 26 to 55. A further 27 benchmarks appeared in the first two quarters of 2026, bringing the corpus to 82; consequently, <strong>56 of the 82 benchmarks (68.3%)</strong> were introduced during 2025–2026.</p>
        <p>This quantitative growth was accompanied by a broadening of evaluation scope. All 29 benchmarks classified under Control Fidelity and Interactive Dynamics and all seven Functional Utility benchmarks were introduced from 2024 onward, while 17 of the 19 Spatial and State Consistency benchmarks appeared in 2025–2026. Long-horizon evaluation is even more recent: nine of the eleven benchmarks in Long-Horizon Memory and State Persistence were released in 2026.</p>
        <p>Meanwhile, Physical Plausibility remained the most densely populated category, comprising 39 benchmarks and expanding from controlled synthetic diagnostics to generative, embodied, and action-conditioned settings. These statistics motivate the four phases summarized in Figure 2: an early emphasis on appearance, physics, and causal reasoning; the emergence of controllability and functional utility from 2024; rapid growth and target diversification in 2025; and the rise of long-horizon and downstream-oriented evaluation in 2026.</p>
      </div>`;
    shell.append(analysis);
  }

  function updateCard(card) {
    const pills = [...card.querySelectorAll(".card-meta .meta-pill")];
    if (pills[1]) setTextIfChanged(pills[1], expandCodes(pills[1].textContent, "Protocol", LABELS.protocol));
    if (pills[2]) setTextIfChanged(pills[2], expandCodes(pills[2].textContent, "Metrics", LABELS.metrics));
    if (pills[3]) setTextIfChanged(pills[3], expandCodes(pills[3].textContent, "Data", LABELS.data));

    const footerLabel = card.querySelector(".card-footer small");
    if (footerLabel) {
      const cleaned = footerLabel.textContent
        .replace(/^Ref\.\s*\[\d+\]\s*·\s*/i, "")
        .trim();
      if (cleaned) setTextIfChanged(footerLabel, cleaned);
      else footerLabel.remove();
    }
  }

  function updateCards(root = document) {
    root.querySelectorAll(".benchmark-card").forEach(updateCard);
  }

  installTimelineAnalysis();

  const grid = document.querySelector("#benchmark-grid");
  if (grid) {
    new MutationObserver(() => updateCards(grid)).observe(grid, {
      childList: true,
      subtree: true,
    });
    updateCards(grid);
  }

  const currentScript = document.currentScript;
  const coreScript = document.createElement("script");
  coreScript.src = new URL("app-v3-core.js?v=5", currentScript?.src || document.baseURI).href;
  coreScript.async = false;
  coreScript.onload = () => {
    installTimelineAnalysis();
    updateCards();
  };
  coreScript.onerror = () => console.error("Could not load app-v3-core.js");
  document.head.append(coreScript);
})();