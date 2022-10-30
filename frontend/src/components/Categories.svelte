<script>
    export let data;
 </script>
 
 <div class="component">
     <h2 class="headText">THE TOTAL OF BOOKS</h2>
     <div class="info-container">
         <div class="info">
             <h1 class="green">{data.readBooks}</h1>
             <h2 class="grey">BOOKS READ</h2>        
         </div>
         <div class="info">
             <h1 class="lightblue">{data.toRead}</h1>
             <h2 class="grey">BOOKS ON READ-LIST</h2>        
         </div>
         <div class="info">
             <h1 class="yellow">{data.currentlyReading}</h1>
             <h2 class="grey">BOOKS READING NOW</h2>        
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
         width: 33%;
     }
 </style>
 
 
 