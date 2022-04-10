import Reac, { useState } from 'react';
import PokemonData from '../components/PokemonData';
import Search from "../components/Search";
import { fetchPokemon } from '../services/pokemon';

export default function HomePage() {
    
    const [pokemon, setPokemon] = useState();
    const [loading, setLoading] = useState(false);

    const getPokemon = async (query) => {
        setLoading(true);
        const response = await fetchPokemon(query);
        console.log(response);
        const results = await response.json();
        console.log(results);
        setPokemon(results);
        setLoading(false);
    }
    return (
        <div>
            <Search getPokemon={getPokemon} />
            { !loading && pokemon ? (
                <div>
                    <PokemonData name={pokemon.name}
                        sprite={pokemon.sprites.front_default}
                        abilities={pokemon.abilities}
                        stats={pokemon.stats}
                        types={pokemon.types}
                        moves={pokemon.moves}
                    />
                </div>
            ): null}
        </div>
    )
}