from abc import ABC, abstractmethod


class AutomationTask(ABC):
    """
    抽象类定义自动化任务的模板。
    """

    def run(self):
        """
        模板方法，定义任务的执行顺序。
        """
        self.setup()
        self.execute()
        self.cleanup()

    @abstractmethod
    def setup(self):
        """
        初始化任务的步骤。在子类中实现具体的初始化逻辑。
        """
        pass

    @abstractmethod
    def execute(self):
        """
        执行任务的步骤。在子类中实现具体的执行逻辑。
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
        清理任务的步骤。在子类中实现具体的清理逻辑。
        """
        pass
