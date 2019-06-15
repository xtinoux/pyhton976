let lst_pasApas = document.querySelectorAll(".pasApas");
lst_pasApas.forEach(function(elt){
	let wrapperHTML = elt.innerHTML;
	elt.innerHTML= "<img class='icone' src='src/images/pas_a_pas.png'/> Le pas  à pas " + wrapperHTML;
	elt.addEventListener("click", function(evt){
			evt.stopPropagation();
			toogleWrapper(elt);
		});
	});

let lst_grandesLignes = document.querySelectorAll(".grandesLignes");
lst_grandesLignes.forEach(function(elt){
	let wrapperHTML = elt.innerHTML;
	elt.innerHTML= "<img  class='icone' src='src/images/checklist2.png'/> Les grandes Lignes " + wrapperHTML;
	
	elt.addEventListener("click", function(evt){
			toogleWrapper(elt);
			evt.stopPropagation();
		});
	});

function toogleWrapper(elt){
	let wrapper = elt.querySelector('.wrapper');
	if (wrapper.classList.contains('invisible'))
	{
		wrapper.classList.remove('invisible');
		wrapper.classList.add('visible');
	}
	else
	{
		wrapper.classList.remove('visible');
				wrapper.classList.add('invisible');
	}
}
