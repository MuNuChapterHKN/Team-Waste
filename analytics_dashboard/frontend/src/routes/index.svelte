<script>
// import BinStats from "$lib/BinStats.svelte";
import ScalarStats from "$lib/ScalarStats.svelte";

</script>
<h1 class='text-2xl font-medium mt-4' >
    This is the homepage
</h1>


<div class='grid grid-cols-6 w-full justify-items-center'>
    <div class='col-span-full'>
        
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
</div>


<style>
</style>