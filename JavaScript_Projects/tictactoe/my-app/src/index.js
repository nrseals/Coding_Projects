import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

//Square Class - renders a button containing the value passed in from props. Constructor method used to initialize state. Button uses onClick event listener to set state value to 'X', causing an X to appear when a square is clicked.
class Square extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: null,
        };
    }
    render() {
        return (
            <button
                className="square"
                onClick={() => this.setState({ value: 'X' })}>
                {this.state.value}
            </button>
        );
    }
}
//Board Class - contains renderSquare method. render declares status constant and returns the value of status, followed by 3 board-rows; each row contains 3 calls of the renderSquare. Constructor lets childen store state values. 
class Board extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            squares: Array(9).fill(null),
        }
    }
    renderSquare(i) {
        return <Square value={this.state.squares[i]} />;
    }

    render() {
        const status = 'Next player: X';

        return (
            <div>
                <div className="status">{status}</div>
                <div className="board-row">
                    {this.renderSquare(0)}
                    {this.renderSquare(1)}
                    {this.renderSquare(2)}
                </div>
                <div className="board-row">
                    {this.renderSquare(3)}
                    {this.renderSquare(4)}
                    {this.renderSquare(5)}
                </div>
                <div className="board-row">
                    {this.renderSquare(6)}
                    {this.renderSquare(7)}
                    {this.renderSquare(8)}
                </div>
            </div>
        );
    }
}
//Game class - renders Board component 
class Game extends React.Component {
    render() {
        return (
            <div className="game">
                <div className="game-board">
                    <Board />
                </div>
                <div className="game-info">
                    <div>{/* status */}</div>
                    <ol>{/* TODO */}</ol>
                </div>
            </div>
        );
    }
}

// ========================================
ReactDOM.render(
    <Game />,
    document.getElementById('root')
);
