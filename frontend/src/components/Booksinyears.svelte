<script>
    export let data;
    import Chart from 'svelte-frappe-charts';
    
    let barColors = ['#9ac1f0']
    let yearsBooks = {
    labels : Object.keys(data.bookYears),
    datasets: [
        {   
            values: Object.values(data.bookYears)
        },
    ],
    yMarkers: [{ label: "Best", value: Math.max.apply(null, Object.values(data.bookYears)),
		options: { labelPos: 'left' }}], 
    };

</script>
 
 <div class="component">
     <h2 class="headText">BOOKS OVER THE YEARS</h2>
     <div class="info-container">
        <div class="info-wide ">
            <Chart data={yearsBooks} type='bar' title="Books read over the Years" colors={barColors} height=500/>
        </div>
         <div class="info">
             <h1 class="green">{Math.max.apply(null, Object.values(data.bookYears))}</h1> 
             <h2 class="grey">MOST BOOKS IN A YEAR</h2>   
         </div>
     </div>
     <p class="note grey">Pre-Year is the books read before the book logging at goodreads</p>    
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
     .note {
        text-align: center;
     }

    
 </style>