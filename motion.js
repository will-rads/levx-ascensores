/* Apply the site preference before CSS loads, so reduced motion never flashes on. */
(() => {
  const systemReduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  let preference = history.state?.levxMotion;
  if (!preference) {
    try { preference = localStorage.getItem("levx-motion"); } catch (_) {}
  }
  const reduced = preference === "off" || (preference !== "on" && systemReduced);
  document.documentElement.dataset.motion = reduced ? "off" : "on";
  document.documentElement.dataset.motionControl = systemReduced || preference === "on" || preference === "off" ? "show" : "hide";
})();
