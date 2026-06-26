import { useEffect, useState } from "react";

function App() {
  const [clusters, setClusters] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:8000/clusters")
      .then((res) => res.json())
      .then((data) => setClusters(data))
      .catch((err) => console.log(err));
  }, []);

  if (!clusters || Object.keys(clusters).length === 0) {
    return (
      <h2 style={{ textAlign: "center", marginTop: "50px" }}>
        ⏳ Loading News...
      </h2>
    );
  }

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      
      <h1 style={{ textAlign: "center", color: "#222" }}>
        📰 News Pulse Dashboard
      </h1>

      {Object.keys(clusters).map((clusterId) => (
        <div key={clusterId} style={{ marginTop: "30px" }}>

          <h2 style={{ color: "#0077ff" }}>
            Cluster {clusterId}
          </h2>

          {clusters[clusterId].map((item, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ddd",
                padding: "10px",
                marginBottom: "10px",
                borderRadius: "8px",
                backgroundColor: "#f9f9f9"
              }}
            >
              <h3>{item.title}</h3>
              <p><b>Source:</b> {item.source}</p>
            </div>
          ))}

        </div>
      ))}
    </div>
  );
}

export default App;