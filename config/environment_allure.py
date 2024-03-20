import platform


class EnvironmentAllure:

    environment = {'OC': platform.platform(),
                   'Python_version': platform.python_version(),
                   'Allure-report.version': '2.23.1',
                   'Database': 'PostgreSQL'
                   }

    @staticmethod
    def create_environment(env=environment):
        with open('environment.properties', 'w', encoding='utf-8') as file:
            for key, value in env.items():
                file.write(f'{key}: {value}' + '\n')
