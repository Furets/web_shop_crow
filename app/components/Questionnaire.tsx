'use client'

import React, {useEffect, useState} from 'react';
import questionsData from '../questionnaire_with_price_fig.json';

// Components

import Figure from './Figure'
import FigureProps from './Figure'

interface Question {
    question: string;
    answers: { [key: string]: any };

    [key: string]: any;
}

interface Figure {
    name: string
    url: string
    price: number
    pricePerMeter: number
    priceForLights: number
    priceForWorkers: number
}

const Questionnaire: React.FC = () => {
    const [currentQuestion, setCurrentQuestion] = useState<Question>(questionsData);
    const [result, setResult] = useState<string>('');
    const [history, setHistory] = useState<Question[]>([]);
    const [SelectedDays, setSelectedDays] = useState<number>(0);
    const [TotalDaysPow, setTotalDaysPow] = useState<number>(10);
    const [totalLenPow, setTotalLenPow] = useState<number>(10);
    const [figures, setFigures] = useState<Figure[]>([]);
    const [showAnswers, setShowAnswers] = useState<boolean>(false);


    useEffect(() => {
        if (currentQuestion.figures) {
            const figures = currentQuestion.figures.map((f: Figure, index: number) => {
                const price = currentQuestion.price[index]
                const pricePerMeter = currentQuestion.price[index]
                const priceForLights = currentQuestion.price_for_lights ? currentQuestion.price_for_lights : 0;
                const priceForWorkers = currentQuestion.price_for_workers[index]
                return {...f, price, pricePerMeter, priceForLights, priceForWorkers};
            })

            setFigures(figures);
        } else {
            setFigures([]);
        }
    }, [currentQuestion]);

    const handleAnswer = (answer: Question | any) => {
        if (answer) {
            if (!answer.result) {
                setHistory([...history, answer]);
            }
            setCurrentQuestion(answer);
        }

        if (answer.result) {
            setResult(answer.result);
        }
    };

    const renderQuestions = () => {
        const questionKeys = ['question_1', 'question_2', 'question_3', 'question_4'];
        let questions: Question[] = [];

        if (currentQuestion.question) {
            questions.push(currentQuestion);
        }

        questionKeys.forEach((key) => {
            if (currentQuestion[key]) {
                questions.push(currentQuestion[key]);
            }
        });

        return (
            <div>
                {questions.map((question, index) => (
                    <div className="mb-4" key={index}>
                        <h2 className="text-xl font-bold">{question.question}</h2>
                        <div className="flex mt-3 flex-row-reverse justify-end">
                            {Object.entries(question.answers).map(([key, value]) => (
                                <button className="btn mr-1" key={key} onClick={() => handleAnswer(value)}>
                                    {key}
                                </button>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        );
    };

    const renderHistory = (): JSX.Element => {
        return (
            <div className="mt-4 text-gray-400">
                <h2>History</h2>
                <ol className="list-decimal ml-4">
                    {history.map((question, index) => (
                        <li key={index}>
                            <h3>
                                {question.question ||
                                    question.question_1.question ||
                                    question.question_2.question ||
                                    question.question_3.question ||
                                    question.question_4.question}
                            </h3>
                        </li>
                    ))}
                </ol>
            </div>
        );
    };

    const RenderDaysSelection = (): JSX.Element => {

        return (
            <div>
                <label htmlFor="small-input" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Hoeveel dagen worden de operaties uitgevoerd?</label>
                <input
                    type="number"
                    className="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    onChange={(e) => setTotalDaysPow(Number(e.target.value))}
                />


                <select
                    id="days"
                    onChange={e => setSelectedDays(Number(e.target.value))}
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                    <option value={0}>dagen</option>
                    <option value={1}>weken</option>
                </select>
                <label htmlFor="days" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Hoelang duurt het weggedeelte waarop de werken zullen worden uitgevoerd?(in meter)</label>
                <input
                    type="number"
                    className="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    onChange={(e) => setTotalLenPow(Number(e.target.value))}
                />
                <br/>
                <button className="btn" onClick={(e) => {
                    setShowAnswers(true)
                }}>
                    Submit
                </button>
            </div>
        );
    };

    const reset = () => {
        setCurrentQuestion(questionsData);
        setHistory([]);
        setResult('');
        // setSelectedDays(null);
    };

    const resetButton = (): JSX.Element => {
        return <button className="btn mr-1" onClick={() => reset()}>Reset</button>;
    };

    return (
        <div>
            {!showAnswers ? (
                RenderDaysSelection()
            ) : (
                <div>
                    {renderQuestions()}
                    {result && (
                        <div>
                            <h2 className="text-xl font-bold">Result</h2>
                            <p>{result}</p>
                            <div className="flex flex-row">
                                {figures.map((figure, index) => (
                                    <div className="basis-1/4" key={index}>
                                        <Figure
                                            figure={figure}
                                            totalLenPow={totalLenPow}
                                            TotalDaysPow={TotalDaysPow}
                                            SelectedDays = {SelectedDays}/>
                                    </div>


                                ))}
                            </div>
                        </div>
                    )}

                    {result && <div className="mt-2">{resetButton()}</div>}
                    {history.length > 0 && renderHistory()}
                </div>
            )}
        </div>
    );
};


export default Questionnaire;
