<script>
  import { selectedColors } from "$lib/utils/colors";
</script>

<div class="overflow-auto flex gap-4 py-5 justify-center items-center">
  {#each $selectedColors as color}
    <div class="flex gap-2">
      <input type="color" bind:value={color} class="mx-auto" />
      <div>{color}</div>
    </div>
  {/each}
  {#if $selectedColors.length < 10}
    <button
      class="btn btn-primary"
      on:click={() => {
        $selectedColors = [...$selectedColors, "#FFD700"];
      }}
    >
      Add
    </button>
  {/if}
  {#if $selectedColors.length > 1}
    <button
      class="btn btn-accent"
      on:click={() => {
        const cs = $selectedColors.slice(0, -1);
        $selectedColors = cs;
      }}>Delete</button
    >
  {/if}
</div>
