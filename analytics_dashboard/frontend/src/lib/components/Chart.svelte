<script lang="ts">
  import Chart from "chart.js/auto";
  import { onMount } from "svelte";

  import type { ChartData, ChartOptions } from "chart.js/auto";

  export let data: ChartData;
  export let options: ChartOptions = {
    responsive: true,
    aspectRatio: 1.9,
  };
  export let type: "line";

  let chartElement;
  let chart: Chart;

  onMount(() => {
    chart = new Chart(chartElement, {
      type,
      data,
      options,
    });
  });

  let updateCount = 0;
  const updateData = (newData: ChartData) => {
    updateCount++;

    console.debug(`updateCount: ${updateCount}`);

    if (updateCount > 1) {
      console.debug("Data was updated");

      chart.data = newData;
      chart.update();
      console.debug("updateData called", updateCount);
    }
  };

  $: updateData(data);
</script>

<div class="relative w-full">
  <canvas bind:this={chartElement} />
</div>
