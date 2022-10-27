<script>
    export let data;
    // https://openlibrary.org/api/books?bibkeys=ISBN:${data.randomTips.ISBN13}&format=json/
    // https://openlibrary.org/api/books?bibkeys=ISBN:${data.randomTips.ISBN13}&format=json
    // https://openlibrary.org/api/books?bibkeys=ISBN:9780980200447&jscmd=data&format=json
    //                {console.log("test", openlibrary[`ISBN:${data.randomTips.ISBN13}`])}
    //                {console.log("test", openlibrary[`ISBN:${data.randomTips.ISBN13}`].cover)}  
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
     <h3 class="headText">5-STAR BOOK TIPS</h3>
     <div class="info-container">
        <div class="info"> 
            <h1 class="green">{data.randomTips.author}</h1>
            <h2>AUTHOR</h2>
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
            <h2>AVERAGE RATING</h2>   
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
        border: 1px red solid;
         width: 33%;
     }
 </style>