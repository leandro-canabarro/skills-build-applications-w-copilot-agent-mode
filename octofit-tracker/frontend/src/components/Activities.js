import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:8000/api/activities/';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch(API_URL)
      .then((response) => response.json())
      .then((data) => {
        console.log('Activities API response:', data);
        const items = Array.isArray(data) ? data : data.results || [];
        setActivities(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Activities fetch error:', err);
        setError('Unable to load activities.');
        setLoading(false);
      });
  }, []);

  return (
    <div className="card shadow-sm border-0 mt-4">
      <div className="card-body">
        <h3 className="card-title mb-3">Activities</h3>
        {loading && <div className="text-muted">Loading activities...</div>}
        {error && <div className="alert alert-danger">{error}</div>}
        {!loading && !error && (
          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle">
              <thead className="table-dark">
                <tr>
                  <th>User</th>
                  <th>Type</th>
                  <th>Duration</th>
                  <th>Distance</th>
                  <th>Points</th>
                </tr>
              </thead>
              <tbody>
                {activities.map((activity) => (
                  <tr key={activity.id ?? activity.completed_at}>
                    <td>{activity.user_details?.display_name || activity.user || 'Unknown'}</td>
                    <td>{activity.activity_type}</td>
                    <td>{activity.duration_minutes} min</td>
                    <td>{activity.distance_km ?? 'N/A'} km</td>
                    <td>{activity.points}</td>
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

export default Activities;
