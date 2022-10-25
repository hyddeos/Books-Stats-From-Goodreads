<script>
  import Totalbooks from './components/Totalbooks.svelte'

  const endpoint = "http://127.0.0.1:8000/api/booksdata/";
  
  let booksData
	
	fetch(endpoint)
		.then(response => { 
		   console.log(' response', response)
		   console.log(' r.json() >', response.clone().json()) //
		   response.json()
			   .then(json => {
						console.log('json', json)
				    booksData = json				   
		     })
		     .catch(error => console.log(error))
	}) 
 </script>

<main>
      {#if booksData}
        MY BOOKS {booksData.readBooks}
        <Totalbooks data={booksData}/>
      {:else}
        <p>loading</p>
      {/if}
</main>

