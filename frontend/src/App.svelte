<script>
  import Totalbooks from './components/Totalbooks.svelte'
  import Booksinyears from './components/Booksinyears.svelte';
  import Randomtips from './components/Randomtips.svelte';
  import Pages from './components/Pages.svelte';
    import Categories from './components/Categories.svelte';

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
      <h1 class="headerText">I <span style="color: red">♥️</span> Books 📖</h1>
      {#if booksData}
        <Totalbooks data={booksData} />
        <Booksinyears data={booksData} />
        <Categories data={booksData} />
        <Pages data={booksData} />
        <Randomtips data={booksData} />
      {:else}
        <p>Loading Book Collection...</p>
      {/if}
</main>

