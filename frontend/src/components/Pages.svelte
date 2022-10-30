<script>
    export let data;

    // Height
    let pagesHeight = data.totalPages * 0.1 / 1000
    pagesHeight = Number(pagesHeight.toFixed(1))
    // Area
    let pagesArea = data.totalPages * (29.7*21) / 10000
    pagesArea = Number(pagesArea.toFixed(0))
    // Weight
    let pagesWeight = data.totalPages * 5.6 / 1000
    pagesWeight = Number(pagesWeight.toFixed(0))

 </script>
 
 <div class="component">
     <h2 class="headText">PAGES</h2>
     <div class="info-container">
         <div class="info">
             <h1 class="green">{data.totalPages}</h1>
             <h2 class="grey">TOTAL PAGES READ</h2>      
         </div>
         <div class="info">
            <h3 class="yellow">{data.longestBook.title}</h3> 
            <h1 class="yellow">{data.longestBook.pages}</h1>
            <h2 class="grey">LONGEST BOOK</h2>                   
         </div>
         <div class="info">
            <h1 class="lightblue">{data.avgPages}</h1>
            <h2 class="grey">BOOK PAGES AVERAGE</h2>
        </div>
     </div>
     <h2 class="headText">IF EVERY PAGE WAS PRINTED...</h2>
     <p class="headText">...on a singlepage A4 page that would be about</p>
     <div class="info-container">        
        <div class="info">
            <h1 class="lightblue">
                {pagesHeight}<span class="grey">m</span></h1>
            <h2 class="grey">HEIGHT</h2>      
        </div>
        <div class="info">
           <h1 class="green">{pagesArea}<span class="grey">m&sup2</span></h1>
           <h2 class="grey">AREA</h2>                   
        </div>
        <div class="info">
           <h1 class="yellow">{pagesWeight}<span class="grey">kg</span></h1>
           <h2 class="grey">WEIGHT</h2>
       </div>
    </div>
 </div>
 
 
 <style>
     .headText {
         text-align: center;
         text-decoration: underline lightpink;
     }
     .info-container {
        width: 100%;
        display: table;
        margin: auto;
        justify-content: center;
        text-align: center;
     }
     .info {
        display: table-cell;
        vertical-align: bottom;
        width: 33%;
     }
 </style>
 
 
 