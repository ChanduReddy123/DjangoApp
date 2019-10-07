module.exports = {
  apps : [{
    name: 'Docker',
    script: 'manage.py',

    // Options reference: https://pm2.io/doc/en/runtime/reference/ecosystem-file/
    args: 'runserver',
    instances: 3,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    }
  }],
};
