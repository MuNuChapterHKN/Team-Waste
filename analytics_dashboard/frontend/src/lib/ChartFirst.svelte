<script lang='ts'>
// import { Chart, registerables } from 'chart.js';
// Chart.register(...registerables);

import Chart from 'chart.js/auto';
import { onMount } from 'svelte';

let chartElem;


const labels = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
];
const data = {
  labels: labels,
  datasets: [{
    label: 'My First dataset',
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    data: [0, 10, 5, 2, 20, 30, 45],
  }]
};

onMount(() => {
    new Chart(chartElem, {
        type: 'line',
        data,
        options: {
            responsive: true,
            maintainAspectRatio: true,
            aspectRatio: 1.4 
        }
    })
})

</script>

<canvas bind:this={chartElem} />
On top of this a chart should get rendered