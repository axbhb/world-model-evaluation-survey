(async () => {
  for (const file of ["app-1.js", "app-2.js", "app-3.js"]) {
    await new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = `assets/${file}`;
      script.onload = resolve;
      script.onerror = () => reject(new Error(`Could not load ${file}`));
      document.head.append(script);
    });
  }
})().catch((error) => console.error(error));
