<script>
   export let data;
</script>

{console.log("i comp", data)}

<div class="component">
    <h3 class="headText">THE TOTAL OF BOOKS</h3>
    <div class="info-container">
        <div class="info">
            <h1 class="green">{data.readBooks}</h1>
            <h2>BOOKS READ</h2>        
        </div>
        <div class="info">
            <h1 class="green">{data.toRead}</h1>
            <h2>BOOKS ON READ-LIST</h2>        
        </div>
        <div class="info">
            <h1 class="green">{data.currentlyReading}</h1>
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


