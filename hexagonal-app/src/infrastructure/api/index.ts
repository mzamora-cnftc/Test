import express from 'express';

const router = express.Router();

// Define your API routes here
router.get('/users', (req, res) => {
    // Logic to get users
    res.send('Get users');
});

router.post('/users', (req, res) => {
    // Logic to create a user
    res.send('Create user');
});

// Export the router
export default router;