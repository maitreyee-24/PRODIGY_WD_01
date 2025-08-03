import React from "react";

export default function WordCloudComponent() {
  return (
    <div>
      <h2>Word Cloud</h2>
      <img
        src="http://127.0.0.1:5000/wordcloud-image"
        alt="Word Cloud"
        style={{ maxWidth: "100%", border: "1px solid #ccc" }}
      />
    </div>
  );
}
