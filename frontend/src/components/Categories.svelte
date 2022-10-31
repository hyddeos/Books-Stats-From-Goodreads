<script>
    export let data;
    import Chart from 'svelte-frappe-charts';

    let maxslices = ['7']
    let colors = ['#f6c445','#9ac1f0','#a0e548', 'lightpink', '#e45f2b']
    let categories = {
    labels : Object.keys(data.categories),
    datasets: [
        {
            values: Object.values(data.categories)
        },
    ],
    };


 </script>
 
 <div class="component">
     <h2 class="headText">CATEGORIES</h2>
     <div class="info-container">
         <div class="info">
            <Chart data={categories} type="pie" colors={colors} maxSlices={maxslices},/>
            <p class="grey">One Book can have more then one category and not all books have categories.</p>               
         </div>
     </div>    
 </div>
 
 
 <style>
     .headText {
         text-align: center;
         text-decoration: underline lightpink;
     }
     .info-container {
         display: flex;
         margin: auto;
         justify-content: center;
         text-align: center;
     }
     .info {
         width: 100%;
     }
 </style>
 
 
 