import { writable } from "svelte/store";

export const selectedColors = writable(["#C0C0C0"]);

// selectedColors.subscribe((cs) => console.debug("Updated colors", cs));
