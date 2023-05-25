import React, { Component, useEffect, useState } from 'react';
import '../assets/css/estacionamento.css'
import axios from 'axios';

const Estacionamento = () => {
    const [item6, setItem6] = useState([0, 1, 2, ])
    const [alocados, setAlocados] = useState([]);
    const [veiculos, setVeiculos] = useState([]);
    const [veiculo, setVeiculo] = useState();
    const [modalArea, setModalArea] = useState(false);
    const [modalVenda, setModalVenda] = useState(false);
    const [idAreaSelecionada, setArea] = useState();
    const [clientes, setClientes] = useState([]);
    const [concessionarias, setCSS] = useState([]);
    const [veiculoId, setVeiculoId] = useState();
    const [cliente, setCliente] = useState("")
    const [concessionaria, setConcessionaria] = useState("")


    useEffect(() => {
        carregarAlocacao();
        carregarClientes();

    }, [])

    const carregarAlocacao = () => {
        axios.get("http://127.0.0.1:5000/alocacao").then((response) => {
            console.log(response)       
            setAlocados(response.data)
        })
    }
    const carregarClientes = () => {
        axios.get("http://127.0.0.1:5000/clientes").then((response) => {
            console.log(response)       
            setClientes(response.data)
        })
    }

    const pesquisar = (id) => {
        if (alocados.length > 0) {
            return alocados.find(x => x.area === id)?.qtd
        }
        else{
            return null
        }
    }

    const selecionarCliente = (value) => {
        setCliente(value)
    }

    const selecionarCSS = (value) => {
        setConcessionaria(value)
    }

    const exibirModal = (id) => {
        console.log('exibir modal')
        console.log(modalArea)
        setModalArea(!modalArea)
        setArea(id)
        axios.get("http://127.0.0.1:5000/alocacao/" + id).then((response) => {
            console.log(response)       
            setVeiculos(response.data)
            
        })
    }

    const vender = (id, veiculo) => {
        setModalArea(false)
        setModalVenda(true)
        setVeiculo(veiculo)
        setVeiculoId(id)
        axios.get("http://127.0.0.1:5000/concessionaria/" + id).then((response) => {
            console.log(response)       
            setCSS(response.data)
            console.log(response.data)
        })


    }
    
    const confirmarVenda = (id) => {
        axios.post("http://127.0.0.1:5000/automovel/" + id).then((res) => {
            console.log(res)
            
            setModalVenda(false)
            
            setVeiculo(res.data)
            
        })
    }

    return ( 
        <>

            <div className={ modalArea ? 'modal-area block' : 'modal-area hidden' } >
                <div className='modal'>
                    Área {idAreaSelecionada}

                    {veiculos.length > 0 ? (
                        veiculos.map((item) => (
                            item.quantidade > 0 &&
                            <div>
                                Modelo: {item.modelo} | Preço { item.preco}
                                <button type='button' onClick={() => vender(item.id, item.modelo)}>
                                    Vender
                                </button>
                            </div>
                        ))
                    ) : null}
                    <button onClick={() => setModalArea(false)}>Fechar</button>
                </div>
            </div>
            <div className={ modalVenda ? 'modal-area block' : 'modal-area hidden' } >
                <div className='modal column'>
                    {veiculo}

                    <div>
                    <select onChange={(e) =>selecionarCliente(e.target.value)}>
                        <option value=""> -- Selecionar Cliente -- </option>
                        {clientes.length > 0 && clientes.map((item) => (
                        <option value={item.id}>{item.Nome}</option>
                        ))}
                    </select>

                     <select onChange={(e) => selecionarCSS(e.target.value)}>
                        <option value=""> -- Selecionar Concessionária -- </option>
                        {concessionarias.length > 0 && concessionarias.map((item) => (
                        <option value={item.id}>{item.nome}</option>
                        ))}
                    </select>                   
                
                    <button onClick={() => confirmarVenda(veiculoId)} disabled={cliente == "" || concessionaria == ""}>Confirmar</button>
                    <button onClick={() => setModalVenda(false)}>Fechar</button>

                    </div>
                </div>
            </div>


            <div className='bloco-8-9-11'>
                <div className='bloco-11'>
                    <div onClick={() => exibirModal(11)} className={'galpao es-8 ' + (pesquisar(8) > 0 ? 'active' : null)}>
                        11
                    </div>
                </div>
                <div className='bloco-89'>
                    <div onClick={() => exibirModal(8)} className={'galpao es-8 ' + (pesquisar(8) > 0 ? 'active' : null)}>
                        8
                    </div>
                    <div onClick={() => exibirModal(9)} className={'galpao es-9 ' + (pesquisar(9) > 0 ? 'active' : null)}>
                        9
                    </div>
                </div>
            </div><div className='base'>
                    <div onClick={() => exibirModal(7)} className={'galpao es-7 ' + (pesquisar(7) > 0 ? 'active' : null)}>
                        7
                    </div>
                    <div onClick={() => exibirModal(4)} className={'galpao es-4 ' + (pesquisar(4) > 0 ? 'active' : null)}>
                        4
                    </div>
                    <div onClick={() => exibirModal(1)} className={'galpao es-1 ' + (pesquisar(1) > 0 ? 'active' : null)} 
                    >
                        1
                    </div>
                    <div onClick={() => exibirModal(3)} className={'galpao es-3 ' + (pesquisar(3) > 0 ? 'active' : null)}>
                        3
                    </div>
                    <div onClick={() => exibirModal(2)} className={'galpao es-2 ' + (pesquisar(2) > 0 ? 'active' : null)} >
                        2

                    </div>
                    <div onClick={() => exibirModal(5)} className={'galpao es-5 ' + (pesquisar(5) > 0 ? 'active' : null)} >
                        5
                    </div>
                </div>
                <div className='direita'>
                    <div className={'galpao es-6 ' + (pesquisar(6) > 0 ? 'active' : null)} 
                        onClick={() => exibirModal(6)}
                    >
                        6 
                    </div>
                    <div onClick={() => exibirModal(10)} className={'galpao es-10 ' + (pesquisar(10) > 0 ? 'active' : null)}>
                        10
                    </div>
                </div>
        
        </>
     );
}
 
export default Estacionamento;