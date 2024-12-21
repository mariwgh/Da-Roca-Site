const testemodal = document.querySelector('.login')
const cads = document.querySelector('.cad')

function abrir(){
    testemodal.showModal()
}
function fechar(){
    testemodal.close()
}
function mostrarSenha(){
    x =  document.querySelector('#senha')
    if (x.type == 'password'){
        x.type = 'text' 
    } else{
        x.type = 'password'
    }
}
function cadastro(){
    cads.showModal()
}
function fechaCad(){
    cads.close()
}

//carrinho a partir daqui--------------------------------------------------
// Define uma variável para armazenar os itens do carrinho, carregando-os do armazenamento local se existirem, caso contrário, inicia como um array vazio
let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
// localStorage.getItem('caritems') pega os dados do cart items armazenados no navegador anteriormente
// e esses dados estão em formato json e o comando json.parse converte eles de json para um formato cujo qual é compatível com JavaScript
// ja na terceira linha--> || é o operador 'ou' ou seja, o let carItemsn faz o json... OU cria um array fazio

// Função para adicionar um item ao carrinho
function addToCart(productName, price) {    //o product name é o nome do produto e o price é o preço, o  progrmaa entnede oq é oq pela ordem dos parametros que está no botão onclick nos produtos
    // Verifica se o item já está no carrinho
    let existingItem = cartItems.find(item => item.name === productName);
    // o find procura algo
    //neste caso a let existingItem verifica se no carrinho ja tem um item com o nome do produto que foi especificado qnd o botão 'adicionar ao carrinho' foi clicado

    if (existingItem) {   //o existingItecm é o result do find
        // Se o item já estiver no carrinho, incrementa a quantidade
        existingItem.quantity++;
    } 
    else {  
        // Se o item ainda não estiver no carrinho, adiciona-o com quantidade 1
        cartItems.push({ name: productName, price: price, quantity: 1 }); 
        // o push adiciona itens ao final de uma array
    }

    // Atualiza a visualização do carrinho
    updateCart();
    // Salva o carrinho no armazenamento local após cada modificação
    saveCartToLocalStorage();
}

// Função para limpar o carrinho
function limparCarrinho() {
    cartItems = []; // Limpa o carrinho
    updateCart(); // Atualiza a visualização do carrinho
    saveCartToLocalStorage(); // Salva o carrinho no armazenamento local após limpar
}

// Função para atualizar a visualização do carrinho
function updateCart() {
    const cartItemsElement = document.getElementById('cartItems'); // Obtém o elemento HTML para os itens do carrinho
    const cartTotalElement = document.getElementById('cartTotal'); // Obtém o elemento HTML para o total do carrinho

    // Limpa os itens do carrinho
    cartItemsElement.innerHTML = '';

    // Adiciona cada item ao carrinho
    cartItems.forEach(item => {   //forEach percorre cada elemento da listacartItems
        const li = document.createElement('li'); // Cria um elemento de lista para cada item
        // Adiciona texto ao elemento de lista com o nome, quantidade e preço total do item
        li.textContent = `${item.name} - Quantidade: ${item.quantity} - R$ ${(item.price * item.quantity).toFixed(2)}`;   //to fixed formata numeros-->quantas casas decimais ele tem
        cartItemsElement.appendChild(li); // Adiciona o elemento de lista ao elemento de itens do carrinho
        //o appendChild é um append só que em html/javaScript
    });

    // Calcula o total do carrinho
    const cartTotal = cartItems.reduce((total, item) => total + (item.price * item.quantity), 0);
    //declaração de varivael-->
    //cmc do numero 0
    //=> escreve funções em comparação com a sintaxe tradicional de função
    //o reduce reduz a um valor aquilo que está nos parenteses: o total é o total até o momento e o item é cada item individual do carrinho, ele multiplica se ha mais de uma quantidade
    //aí o resto calcula o valor total

    // Atualiza o elemento HTML para mostrar o total do carrinho
    cartTotalElement.textContent = cartTotal.toFixed(2);
    //oq ta dentro da variavel em forma de texto
    //declarada la em cima
}

// Função para salvar o carrinho no armazenamento local
function saveCartToLocalStorage() {
    localStorage.setItem('cartItems', JSON.stringify(cartItems)); 
    // Salva os itens do carrinho no armazenamento local como uma string JSON
}

// para aparecer a telinha em overlay
// Obtém o elemento HTML para o modal do carrinho
const car = document.getElementById('carrinho');

// Função para mostrar o modal do carrinho
function mostrarCarrinho() {
    car.showModal();
}

// Função para fechar o modal do carrinho
function fechaCarrinho() {
    car.close();
}

// Executa a função updateCart quando a página é carregada para exibir os itens do carrinho salvos
window.addEventListener('DOMContentLoaded', updateCart);

//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Obtém a referência para a div fim
const fimDiv = document.getElementById('fim');

// Função para exibir os itens do carrinho na div fim
function exibirItensNoFim() {
    // Limpa o conteúdo da div fim
    fimDiv.innerHTML = '';

    // Cria uma lista não ordenada para exibir os itens do carrinho
    const ul = document.createElement('ul');

    // Adiciona cada item do carrinho à lista
    //o forEach percorre cada item da lista
    cartItems.forEach(item => {
        const li = document.createElement('li');        //-->declara variavel
        li.textContent = `${item.name} - Quantidade: ${item.quantity} - R$ ${(item.price * item.quantity).toFixed(2)}`;
        //na linha de cima o li.textContent adiciona o nome dos itens, a quantidade e o preço
        ul.appendChild(li);
        //na linha de cima  o li é aidionado como elemento filho do ul
    });

    // Adiciona a lista à div fim
    fimDiv.appendChild(ul);

    // Calcula e exibe o total do carrinho na div fim
    const cartTotal = cartItems.reduce((total, item) => total + (item.price * item.quantity),0);
    //o 0 é o valor inicial para o cálculo total
    const totalParagraph = document.createElement('p');
    //o parágrafo é para quebrar a linha
    totalParagraph.textContent = `Total: R$ ${cartTotal.toFixed(2)}`;       //o $ é como se fosse o f da formatação de string em python
    //nesse parágrafo é adicionado um texto cujo é o total
    fimDiv.appendChild(totalParagraph);
    //aqui a var totalParagraph é adicionada a div fim
}

// Chama a função para exibir os itens do carrinho na div fim
exibirItensNoFim();
