<script>
    export let data;
 </script>
 
 <div class="component">
     <h2 class="headText">COST OF BOOKS READ</h2>
     <p class="headerText">The estimated price for All books if bought from Amazon</p>
     <div class="info-container">
        
         <div class="info">
             <h1 class="lightblue">{data.prices.estimatedPrice}<span class="grey">kr</span></h1>
             <h2 class="grey">TOTAL COST OF BOOKS</h2>        
         </div>
         <div class="info">
             <h1 class="green">{data.prices.avgPrice}<span class="grey">kr</span></h1>
             <h2 class="grey">AVERAGE BOOK PRICE</h2>        
         </div>
     </div>
     <p class="headerText grey">Book prices is scrapped of Amazon and based on first result which might not always be correct.</p>
     <p class="headerText grey">For the <span class="yellow">{data.prices.withoutPrices}</span> of <span class="yellow">{data.prices.withPrices}</span> books without a price has still been added to the total estimated cost with the average price</p>
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
         width: 33%;
     }
 </style>
 
 
 