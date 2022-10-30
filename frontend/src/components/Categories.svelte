<script>
    export let data;
    import Chart from 'svelte-frappe-charts';


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
            <Chart data={categories} type="donut"/>
            <p class="grey">One Book can have more then one category</p>               
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
 
 
 