import React from 'react';

interface FigureProps {
    figure: {
        url: string
        name: string
        totalPrice: number
    }
}

const Figure: React.FC<FigureProps> = (props) => {
    return <div className="mx-1 my-1">
        <h4>{props.figure.name}</h4>
        <img src={props.figure.url}/>
        <p>{props.figure.totalPrice}</p>
        <button className="btn">Price</button>
    </div>
};

export default Figure