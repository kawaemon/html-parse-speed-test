const begin_time = performance.now();
const result_element = document.querySelector(".render_time");

window.addEventListener("load", () => {
  const render_time = performance.now() - begin_time;
  const text = "render time: " + render_time + "ms";

  console.log(text);
  result_element.innerHTML = text;
});
