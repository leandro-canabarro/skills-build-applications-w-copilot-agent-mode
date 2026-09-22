import { BrowserRouter, NavLink, Route, Routes } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <BrowserRouter>
      <div className="app-shell">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
          <div className="container">
            <span className="navbar-brand fw-bold">OctoFit Tracker</span>
            <div className="navbar-nav ms-auto">
              <NavLink className="nav-link" to="/">Overview</NavLink>
              <NavLink className="nav-link" to="/users">Users</NavLink>
              <NavLink className="nav-link" to="/teams">Teams</NavLink>
              <NavLink className="nav-link" to="/activities">Activities</NavLink>
              <NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink>
              <NavLink className="nav-link" to="/workouts">Workouts</NavLink>
            </div>
          </div>
        </nav>

        <main className="container py-4">
          <Routes>
            <Route
              path="/"
              element={
                <div className="row g-4">
                  <div className="col-lg-3 col-md-6">
                    <div className="stat-card accent-blue">
                      <span className="stat-label">Active athletes</span>
                      <h2>128</h2>
                    </div>
                  </div>
                  <div className="col-lg-3 col-md-6">
                    <div className="stat-card accent-green">
                      <span className="stat-label">Teams</span>
                      <h2>12</h2>
                    </div>
                  </div>
                  <div className="col-lg-3 col-md-6">
                    <div className="stat-card accent-orange">
                      <span className="stat-label">Workout plans</span>
                      <h2>24</h2>
                    </div>
                  </div>
                  <div className="col-lg-3 col-md-6">
                    <div className="stat-card accent-purple">
                      <span className="stat-label">Average points</span>
                      <h2>1,420</h2>
                    </div>
                  </div>

                  <div className="col-12">
                    <div className="card shadow-sm border-0">
                      <div className="card-body">
                        <h3 className="card-title mb-3">Welcome back, coach</h3>
                        <p className="mb-0 text-muted">
                          Track training progress, monitor team momentum, and review the leaderboard to keep your athletes improving.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              }
            />
            <Route path="/users" element={<Users />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
