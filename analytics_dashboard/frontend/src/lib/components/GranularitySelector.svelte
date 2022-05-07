<script lang="ts">
  import { createEventDispatcher } from "svelte/internal";

  import type { Granularity } from "./ChronChart.svelte";
  export let options: Granularity[];

  let selected = options[0] ?? null;

  const dispatch = createEventDispatcher();
  const onClick = (option) => {
    dispatch("change", option);
    selected = option;
  }
</script>

<div class="tabs">
{#each options as option}
  <div class="tab tab-bordered" class:tab-active={option === selected} on:click={() => onClick(option)} >{option.toString()}</div>
{/each}
</div>
