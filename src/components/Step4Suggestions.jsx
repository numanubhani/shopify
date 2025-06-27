import React, { useEffect, useState } from "react";

export default function Step4Suggestions({ email, onNext }) {
    const [suggestions, setSuggestions] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Simulate async fetch delay
        const timeout = setTimeout(() => {
            setSuggestions({
                summary: "A minimal yet versatile wardrobe of elevated basics.",
                colors: ["Black", "Ivory", "Olive", "Dusty Rose"],
                fabrics: ["Organic Cotton", "Linen", "Modal", "Recycled Polyester"],
                tips: "Focus on clean lines, durable stitching, and fabric sustainability.",
            });
            setLoading(false);
        }, 1000); // Simulate delay

        return () => clearTimeout(timeout);
    }, []);

    if (loading) {
        return (
            <div className="text-center text-white/70 mt-20 font-sans">
                Thinking like a fashion expert...
            </div>
        );
    }

    const colorList = Array.isArray(suggestions.colors)
        ? suggestions.colors
        : suggestions.colors?.split(",") || [];

    const fabricList = Array.isArray(suggestions.fabrics)
        ? suggestions.fabrics
        : suggestions.fabrics?.split(",") || [];

    return (
        <div className="max-w-2xl mx-auto mt-10 p-8 border border-white bg-black/40 backdrop-blur-md rounded-lg shadow-lg font-sans text-white">
            <h2 className="text-3xl font-normal mb-4">Smart Suggestions</h2>
            <p className="text-sm text-white/70 mb-8">
                Based on your input, here’s what we recommend:
            </p>

            <div className="mb-6">
                <h3 className="text-base font-semibold mb-2">Capsule Summary</h3>
                <p className="border border-white p-3 bg-white/10 rounded">
                    {suggestions.summary}
                </p>
            </div>

            <div className="mb-6">
                <h3 className="text-base font-semibold mb-2">Suggested Colors</h3>
                <ul className="list-disc pl-5 text-sm space-y-1">
                    {colorList.map((color, i) => (
                        <li key={i}>{color.trim()}</li>
                    ))}
                </ul>
            </div>

            <div className="mb-6">
                <h3 className="text-base font-semibold mb-2">Recommended Fabrics</h3>
                <ul className="list-disc pl-5 text-sm space-y-1">
                    {fabricList.map((fabric, i) => (
                        <li key={i}>{fabric.trim()}</li>
                    ))}
                </ul>
            </div>

            <div className="mb-10">
                <h3 className="text-base font-semibold mb-2">Construction Tips</h3>
                <p className="text-sm">{suggestions.tips}</p>
            </div>

            <button
                onClick={onNext}
                className="px-6 py-2 text-sm font-medium text-white border border-white bg-transparent hover:bg-white hover:text-black transition duration-200 rounded"
            >
                Next →
            </button>
        </div>
    );
}
