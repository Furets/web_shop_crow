'use client'

import React, {useEffect, useState} from 'react';
import questionsData from '../questionnaire_with_price_fig.json';

// Components

import Figure from './Figure'

interface Question {
    question: string;
    answers: { [key: string]: any };

    [key: string]: any;
}

interface Figure {
    name: string
    url: string
}

const Questionnaire: React.FC = () => {
    const [currentQuestion, setCurrentQuestion] = useState<Question>(questionsData);
    const [result, setResult] = useState<string>('');
    const [history, setHistory] = useState<Question[]>([]);
    const [selectedDays, setSelectedDays] = useState<number | null>(null);
    const [totalPricePow, setTotalPricePow] = useState<number>(10);
    const [totalLen, settotalLen] = useState<number>(10);
    const [figures, setFigures] = useState<{ url: string; name: string; totalPrice: number; }[]>([]);;

    useEffect(() => {
    if (currentQuestion.figures) {
        const figures = currentQuestion.figures.map((f: Figure, index: number) => {
            // Check if currentQuestion has price_for_lights; if not, set it to 0
            const priceForLights = currentQuestion.price_for_lights ? currentQuestion.price_for_lights : 0;
            const totalPrice = totalPricePow * (currentQuestion.price[index] + totalLen * (currentQuestion.price_per_meter[index] + priceForLights) + currentQuestion.price_for_workers[index]);
            return { ...f, totalPrice };
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

    const handleDaysSelection = (days: number) => {
        setSelectedDays(days);
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

    const renderDaysSelection = (): JSX.Element => {
        return (
            <div>
                <label htmlFor="days">Hoeveel dagen worden de operaties uitgevoerd?</label>
                <input type="number" className="text-black" onChange={(e) => setTotalPricePow(Number(e.target.value))} />
                <select
                    id="days"
                    value={selectedDays !== null ? selectedDays.toString() : ''}
                    onChange={(e) => handleDaysSelection(Number(e.target.value))}
                >
                    <option value={1}>-</option>
                    <option value={2}>dagen</option>
                    <option value={1}>weken</option>
                </select>
                <br/> {/* Add a line break */}
                <button className="btn" onClick={() => handleAnswer({days: selectedDays})}>Submit</button>
            </div>
        );
    };


    const reset = () => {
        setCurrentQuestion(questionsData);
        setHistory([]);
        setResult('');
        setSelectedDays(null);
    };

    const resetButton = (): JSX.Element => {
        return <button className="btn mr-1" onClick={() => reset()}>Reset</button>;
    };

    // @ts-ignore
    // @ts-ignore
    // @ts-ignore
    // @ts-ignore
    // @ts-ignore
    // @ts-ignore
    return (
        <div>
            {selectedDays === null ? (
                renderDaysSelection()
            ) : (
                <>
                    {renderQuestions()}
                    {result && (
                        <div>
                            <h2 className="text-xl font-bold">Result</h2>
                            <p>{result}</p>
                            <div className="flex flex-row">
                                {figures.map((figure, index) => (
                                    <div className="basis-1/4" key={index}>
                                        <Figure figure = {figure}  />
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {result && <div className="mt-2">{resetButton()}</div>}
                    {history.length > 0 && renderHistory()}
                </>
            )}
        </div>
    );
};


export default Questionnaire;
