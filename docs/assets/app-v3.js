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

  function updateCard(card) {
    const pills = [...card.querySelectorAll(".card-meta .meta-pill")];
    if (pills[1]) pills[1].textContent = expandCodes(pills[1].textContent, "Protocol", LABELS.protocol);
    if (pills[2]) pills[2].textContent = expandCodes(pills[2].textContent, "Metrics", LABELS.metrics);
    if (pills[3]) pills[3].textContent = expandCodes(pills[3].textContent, "Data", LABELS.data);

    const footerLabel = card.querySelector(".card-footer small");
    if (footerLabel) {
      footerLabel.textContent = footerLabel.textContent
        .replace(/^Ref\.\s*\[\d+\]\s*·\s*/i, "")
        .trim();
      if (!footerLabel.textContent) footerLabel.remove();
    }
  }

  function updateCards(root = document) {
    root.querySelectorAll(".benchmark-card").forEach(updateCard);
  }

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
  coreScript.onload = () => updateCards();
  coreScript.onerror = () => console.error("Could not load app-v3-core.js");
  document.head.append(coreScript);
})();
