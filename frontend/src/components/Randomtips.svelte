<script>
    export let data;

    const openlibraryURL = `https://openlibrary.org/api/books?bibkeys=ISBN:${data.randomTips.ISBN13}&jscmd=data&format=json`;

    let openlibrary
    fetch(openlibraryURL)
		.then(response => { 
		   console.log(' Response', response)
		   console.log(' r.json() >', response.clone().json()) //
		   response.json()
			   .then(json => {
					console.log('json', json)
				    openlibrary = json				   
		     })
		     .catch(error => console.log(error))        
	})

    
 </script> 
 
 <div class="component">
     <h2 class="headText">5-STAR BOOK TIPS</h2>
     <p class="headText">A randomly selected book from all my 5-Star rated books</p>
     <div class="info-container">
        <div class="info">

            <h1 class="green">{data.randomTips.author}</h1>
            <h2 class="grey">AUTHOR</h2>
        </div>
        <div class="info">
            {#if openlibrary}              
                <img src={openlibrary[`ISBN:${data.randomTips.ISBN13}`].cover.large} alt="Random 5-star Book recommendation" />
            {:else}
                <h4>Did not find any book cover</h4>
            {/if}
            <h2>{data.randomTips.title}</h2>     
        </div>
         <div class="info">      
            <h1 class="lightblue">{data.randomTips.avgRating}</h1>
            <h2 class="grey">AVERAGE RATING</h2>   
         </div>
     </div>
 </div>
 
 
 <style>
     .headText {
         text-align: center;
     }
     .info-container {
        display: table;
        margin: auto;
        justify-content: center;
        text-align: center;
     }
     .info {
        display: table-cell;
        text-align: center;
        vertical-align: middle;
        width: 33%;
     }
 </style>