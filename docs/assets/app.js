(() => {
  const script = document.createElement("script");
  script.src = "assets/app-v2.js";
  script.defer = true;
  script.onerror = () => console.error("Could not load app-v2.js");
  document.head.append(script);
})();
