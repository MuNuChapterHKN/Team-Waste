<script>
// import BinStats from "$lib/BinStats.svelte";
import ChartFirst from "$lib/ChartFirst.svelte";
import ScalarStats from "$lib/ScalarStats.svelte";

</script>
<h1 class='text-2xl font-medium mt-4' >
    This is the homepage
</h1>


<div class='grid sm:grid-cols-6 md:grid-cols-9 w-full justify-items-center'>
    <div class='col-span-full justify-self-center'>
        
        <ScalarStats queries={[
            {
                title: "Number of bins",
                query: { measures: ['Bin.count'] }
            },
            {
                title: "Number of islands",
                query: { measures: ['Island.count'] }
            }
        ]}></ScalarStats>

    </div>
    
    <div class='col-span-3 justify-self-center'>
        <ChartFirst />
    </div>
    <div class='col-span-3 justify-self-center'>
        <ChartFirst />
    </div>
    <div class='col-span-3 justify-self-center'>
        <ChartFirst />
    </div>
    <div class='col-span-3 justify-self-center'>
        <ChartFirst />
    </div>
    <div class='col-span-3 justify-self-center'>
        <ChartFirst />
    </div>
    <div class='col-span-3 justify-self-center'>
        <ChartFirst />
    </div>

</div>
