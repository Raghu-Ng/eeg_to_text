import React, { useState } from "react";
import axios from "axios";
import { Button, TextField, Typography, Box } from "@mui/material";

function App() {
  const [file, setFile] = useState(null);
  const [predictedText, setPredictedText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handlePredict = async () => {
    if (!file) {
      alert("Please upload an EEG signal file.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("eeg_file", file);

    try {
      const response = await axios.post("http://localhost:5000/predict", formData);
      setPredictedText(response.data.text);
    } catch (error) {
      console.error("Error during prediction:", error);
      alert("Prediction failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleTextToSpeech = () => {
    const utterance = new SpeechSynthesisUtterance(predictedText);
    window.speechSynthesis.speak(utterance);
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh",
        padding: "20px",
      }}
    >
      <Typography variant="h4" gutterBottom>
        Thought-to-Text Conversion
      </Typography>
      <TextField
        type="file"
        onChange={handleFileChange}
        sx={{ marginBottom: "20px" }}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handlePredict}
        disabled={loading}
      >
        {loading ? "Processing..." : "Predict"}
      </Button>
      {/* {predictedText && (
        <>
          <Typography variant="h6" sx={{ marginTop: "20px" }}>
            Predicted Text: {predictedText}
          </Typography>
          <Button
            variant="outlined"
            color="secondary"
            onClick={handleTextToSpeech}
          >
            Play Speech
          </Button>
        </>
      )} */}

        {predictedText && (
          <>
            <Typography
              variant="h1"
              sx={{
                marginTop: "20px",
                fontWeight: "bold",
                color: "blue",
                textAlign: "center",
              }}
            >
              {predictedText}
            </Typography>
            <Button
              variant="outlined"
              color="secondary"
              onClick={handleTextToSpeech}
              sx={{ marginTop: "20px" }}
            >
              Play Speech
            </Button>
          </>
        )}


    </Box>
  );
}

export default App;
