<script>
   export let data;
</script>



<div class="component">
    <h3 class="headText">THE TOTAL OF BOOKS</h3>
    <div class="info-container">
        <div class="info">
            <h1 class="green">{data.readBooks}</h1>
            <h2>BOOKS READ</h2>        
        </div>
        <div class="info">
            <h1 class="lightblue">{data.toRead}</h1>
            <h2>BOOKS ON READ-LIST</h2>        
        </div>
        <div class="info">
            <h1 class="yellow">{data.currentlyReading}</h1>
            <h2>BOOKS READING NOW</h2>        
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


