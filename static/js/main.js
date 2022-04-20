const dolarC = document.querySelector(".dolarCompra").firstChild.data;
const dolarV = document.querySelector(".dolarVenta").firstChild.data;

const dolarCo = dolarC.slice(1)
const dolarVe = dolarV.slice(1)

const dolarCompra = parseInt(dolarCo);
const dolarVenta = parseInt(dolarVe);

console.log(dolarCompra, dolarVenta);

const getValueInput = ()=>{
    let inputValue = document.querySelector('.ingresarValor').value;
    let select = document.querySelector('.menuSelect');
    let value = select.options[select.selectedIndex].value;
    if (value == 1){
        var conversion = inputValue * dolarVenta;
        document.querySelector(".valueInput").innerHTML = `Tenes: $${conversion} Pesos`;
    }
    else if (value == 2){
        var valor = inputValue / dolarVenta
        var conversion = Number(valor.toFixed(2))
        document.querySelector(".valueInput").innerHTML = `Tenes: $${conversion} Dolares`
    }

}
