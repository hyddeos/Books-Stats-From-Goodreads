<script>
    export let data;
</script>
 
 
 <div class="component">
     <h3 class="headText">BOOKS OVER THE YEARS</h3>
     <div class="info-container">
         <div class="info">
             <h1 class="green">{data.firstYear}</h1>
             <h2>first year</h2>   
         </div>
         <div>

         </div>
     </div>    
 </div>
 
 
 <style>
     .headText {
         text-align: center;
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