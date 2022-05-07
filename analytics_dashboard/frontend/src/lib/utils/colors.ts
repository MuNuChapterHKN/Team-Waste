import { writable } from "svelte/store";

const debounce = (func, timeout = 250) => {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => func.apply(this, args), timeout);
  };
};

const debouncedWritable = (initialValue) => {
  const { set, update, subscribe } = writable(initialValue);

  return {
    set: debounce(set),
    update,
    subscribe,
  };
};

export const selectedColors = debouncedWritable([
  "#C0C0C0",
  "#FFD700",
  "#00ff6e",
  "#e100ff",
  "#3a5ad9",
]);
