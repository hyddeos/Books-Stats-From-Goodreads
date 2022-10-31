<script>
    export let data;
    import Chart from 'svelte-frappe-charts';

 
    let colors = ['#f6c445']
    let maxslices = ['12']
    let months = {
    labels : Object.keys(data.months[0]),
    datasets: [
        { type:'line', name:"2018", values: Object.values(data.months[1].year2018), },
        { type:'line', name:"2019", values: Object.values(data.months[1].year2019), },
        { type:'line', name:"2020", values: Object.values(data.months[1].year2020), },
        { type:'line', name:"2021", values: Object.values(data.months[1].year2021), },
        { type:'line', name:"2022", values: Object.values(data.months[1].year2022), },
    ],
    };
    let monthsTotal = {
    labels : Object.keys(data.months[0]),
    datasets: [
        { type:'percentage', name:"Books Per Month Total", values: Object.values(data.months[0]), },

    ],
    };
    console.log("tesdt",data.months[1]  )
</script>
 
 <div class="component">
     <h2 class="headText">BOOKS OVER THE MONTHS</h2>
     <div class="info-container">
        <div class="info-wide ">
            <Chart data={months} type='axis-mixed' height=500 title="Books read over the Months" colors={colors} />
            <Chart data={monthsTotal} type='percentage' height=170 title="Number of books per month total over all years" colors={colors} maxSlices={maxslices}/>
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
         width: 20%;
     }
     .info-wide{
        width: 80%;
     }

    
 </style>