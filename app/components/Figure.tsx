import React, { useState } from 'react';

interface FigureProps {
  figure: {
    url: string;
    name: string;
    price: number;
    pricePerMeter: number;
    priceForLights: number;
    priceForWorkers: number;
  };
  TotalDaysPow: number;
  totalLenPow: number;
  SelectedDays: number;
}

const Figure: React.FC<FigureProps> = (props) => {
  const [inputWorkerHours, setInputWorkerHours] = useState<number>(0);

  const pricePerMeter =
    props.SelectedDays === 0 ? props.figure.pricePerMeter / 3 : props.figure.pricePerMeter;

  const priceForLights = props.figure.priceForLights;
  const priceForWorkers = props.figure.priceForWorkers;
  const totalPrice =
    props.TotalDaysPow *
    (props.totalLenPow * (pricePerMeter + priceForLights) + props.figure.price) +
    inputWorkerHours * priceForWorkers;

  return (
    <div className="mx-1 my-1">
      <h4>{props.figure.name}</h4>
      <img src={props.figure.url} alt={props.figure.name} />
      <ul>
        <li>Price: {Math.round(props.figure.price)}</li>
        <li>Price Per Meter: {Math.round(pricePerMeter)}</li>
        <li>Price For Lights: {Math.round(priceForLights)}</li>
        <li>Price For Worker Hour: {Math.round(priceForWorkers)}</li>
        <li>Total price: {Math.round(totalPrice)}</li>
      </ul>

      <div>
        <label htmlFor="worker-hours" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
          Worker Hours
        </label>
        <input
          type="number"
          id="worker-hours"
          className="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          value={inputWorkerHours}
          onChange={(e) => setInputWorkerHours(Number(e.target.value))}
        />
      </div>
    </div>
  );
};

export default Figure;
