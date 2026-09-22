import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:8000/api/users/';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch(API_URL)
      .then((response) => response.json())
      .then((data) => {
        console.log('Users API response:', data);
        const items = Array.isArray(data) ? data : data.results || [];
        setUsers(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Users fetch error:', err);
        setError('Unable to load users.');
        setLoading(false);
      });
  }, []);

  return (
    <div className="card shadow-sm border-0 mt-4">
      <div className="card-body">
        <h3 className="card-title mb-3">Users</h3>
        {loading && <div className="text-muted">Loading users...</div>}
        {error && <div className="alert alert-danger">{error}</div>}
        {!loading && !error && (
          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle">
              <thead className="table-dark">
                <tr>
                  <th>Username</th>
                  <th>Email</th>
                  <th>Fitness level</th>
                  <th>Display name</th>
                </tr>
              </thead>
              <tbody>
                {users.map((user) => (
                  <tr key={user.id ?? user.username}>
                    <td>{user.username}</td>
                    <td>{user.email || 'N/A'}</td>
                    <td>{user.fitness_level || 'beginner'}</td>
                    <td>{user.display_name || user.first_name || 'N/A'}</td>
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

export default Users;
