import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:8000/api/leaderboard/';

function Leaderboard() {
  const [scores, setScores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch(API_URL)
      .then((response) => response.json())
      .then((data) => {
        console.log('Leaderboard API response:', data);
        const items = Array.isArray(data) ? data : data.results || [];
        setScores(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Leaderboard fetch error:', err);
        setError('Unable to load leaderboard.');
        setLoading(false);
      });
  }, []);

  return (
    <div className="card shadow-sm border-0 mt-4">
      <div className="card-body">
        <h3 className="card-title mb-3">Leaderboard</h3>
        {loading && <div className="text-muted">Loading leaderboard...</div>}
        {error && <div className="alert alert-danger">{error}</div>}
        {!loading && !error && (
          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle">
              <thead className="table-dark">
                <tr>
                  <th>Rank</th>
                  <th>User</th>
                  <th>Points</th>
                </tr>
              </thead>
              <tbody>
                {scores.map((entry) => (
                  <tr key={entry.id ?? entry.user}>
                    <td>{entry.rank}</td>
                    <td>{entry.user_details?.display_name || entry.user || 'Unknown'}</td>
                    <td>{entry.points}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default Leaderboard;
