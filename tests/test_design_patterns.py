from algorithms.design_patterns.singleton import SingletonMeta
from algorithms.design_patterns.factory_method import AnimalFactory
from algorithms.design_patterns.abstract_factory import PetFactory
from algorithms.design_patterns.builder import PizzaBuilder
from algorithms.design_patterns.prototype import Prototype
from algorithms.design_patterns.adapter import (
    Dog as AdapterDog, Cat as AdapterCat, DogAdapter, CatAdapter
)
from algorithms.design_patterns.decorator import (
    TextComponent, BoldDecorator, ItalicDecorator
)
from algorithms.design_patterns.facade import ComputerFacade
from algorithms.design_patterns.proxy import RealSubject, ProtectionProxy
from algorithms.design_patterns.composite import Leaf, Composite
from algorithms.design_patterns.observer import Subject, ConcreteObserver
from algorithms.design_patterns.strategy import (
    AddStrategy, SubtractStrategy, MultiplyStrategy, Context
)
from algorithms.design_patterns.command import PrintCommand, Invoker
from algorithms.design_patterns.template_method import HTMLReport, TextReport
from algorithms.design_patterns.state import Door
from algorithms.design_patterns.chain_of_responsibility import ConcreteHandler

import unittest


class TestSingleton(unittest.TestCase):
    def test_single_instance(self):
        class MyClass(metaclass=SingletonMeta):
            pass
        a = MyClass()
        b = MyClass()
        self.assertIs(a, b)

    def test_different_classes(self):
        class A(metaclass=SingletonMeta):
            pass
        class B(metaclass=SingletonMeta):
            pass
        self.assertIsNot(A(), B())


class TestFactoryMethod(unittest.TestCase):
    def test_create_dog(self):
        dog = AnimalFactory.create_animal("dog")
        self.assertEqual(dog.speak(), "Woof!")

    def test_create_cat(self):
        cat = AnimalFactory.create_animal("cat")
        self.assertEqual(cat.speak(), "Meow!")

    def test_unknown_animal(self):
        with self.assertRaises(ValueError):
            AnimalFactory.create_animal("fish")


class TestAbstractFactory(unittest.TestCase):
    def test_create_pet_and_toy(self):
        factory = PetFactory()
        dog = factory.create_pet("dog")
        toy = factory.create_toy("dog")
        self.assertEqual(dog.speak(), "Woof!")
        self.assertEqual(toy.play(), "Squeak!")

    def test_create_cat_and_toy(self):
        factory = PetFactory()
        cat = factory.create_pet("cat")
        toy = factory.create_toy("cat")
        self.assertEqual(cat.speak(), "Meow!")
        self.assertEqual(toy.play(), "Rattle!")

    def test_unknown_pet(self):
        factory = PetFactory()
        with self.assertRaises(ValueError):
            factory.create_pet("fish")


class TestBuilder(unittest.TestCase):
    def test_build_pizza(self):
        builder = PizzaBuilder()
        pizza = (builder
                 .set_size("large")
                 .add_cheese()
                 .add_pepperoni()
                 .build())
        self.assertEqual(pizza.size, "large")
        self.assertIn("cheese", pizza.toppings)
        self.assertIn("pepperoni", pizza.toppings)

    def test_builder_resets(self):
        builder = PizzaBuilder()
        builder.set_size("small").add_cheese().build()
        pizza2 = builder.set_size("medium").build()
        self.assertEqual(pizza2.size, "medium")
        self.assertEqual(pizza2.toppings, [])


class TestPrototype(unittest.TestCase):
    def test_clone(self):
        proto = Prototype()
        proto.register("car", {"brand": "Unknown", "speed": 0})
        car = proto.clone("car")
        self.assertEqual(car["brand"], "Unknown")

    def test_clone_is_deep_copy(self):
        proto = Prototype()
        proto.register("list", {"items": [1, 2, 3]})
        clone = proto.clone("list")
        clone["items"].append(4)
        original = proto.clone("list")
        self.assertEqual(len(original["items"]), 3)


class TestAdapter(unittest.TestCase):
    def test_dog_adapter(self):
        dog = AdapterDog()
        adapted = DogAdapter(dog)
        self.assertEqual(adapted.make_noise(), "Woof!")

    def test_cat_adapter(self):
        cat = AdapterCat()
        adapted = CatAdapter(cat)
        self.assertEqual(adapted.make_noise(), "Meow!")


class TestDecorator(unittest.TestCase):
    def test_bold_decorator(self):
        component = TextComponent("Hello")
        bold = BoldDecorator(component)
        self.assertEqual(bold.render(), "<b>Hello</b>")

    def test_italic_decorator(self):
        component = TextComponent("Hello")
        italic = ItalicDecorator(component)
        self.assertEqual(italic.render(), "<i>Hello</i>")

    def test_stacked_decorators(self):
        component = TextComponent("Hello")
        bold_italic = BoldDecorator(ItalicDecorator(component))
        self.assertEqual(bold_italic.render(), "<b><i>Hello</i></b>")


class TestFacade(unittest.TestCase):
    def test_start(self):
        computer = ComputerFacade()
        result = computer.start()
        self.assertEqual(result, "CPU started. Memory loaded. Disk reading.")


class TestProxy(unittest.TestCase):
    def test_valid_password(self):
        real = RealSubject()
        proxy = ProtectionProxy(real, "secret")
        self.assertEqual(proxy.request("secret"),
                         "RealSubject: handling request")

    def test_invalid_password(self):
        real = RealSubject()
        proxy = ProtectionProxy(real, "secret")
        self.assertEqual(proxy.request("wrong"), "Proxy: access denied")


class TestComposite(unittest.TestCase):
    def test_leaf(self):
        leaf = Leaf("A")
        self.assertEqual(leaf.get_info(), "A")

    def test_composite(self):
        leaf1 = Leaf("A")
        leaf2 = Leaf("B")
        composite = Composite("root")
        composite.add(leaf1)
        composite.add(leaf2)
        self.assertEqual(composite.get_info(), "root: [A, B]")

    def test_nested_composite(self):
        leaf1 = Leaf("A")
        child = Composite("child")
        child.add(leaf1)
        root = Composite("root")
        root.add(child)
        self.assertEqual(root.get_info(), "root: [child: [A]]")


class TestObserver(unittest.TestCase):
    def test_notify(self):
        subject = Subject()
        obs1 = ConcreteObserver("obs1")
        obs2 = ConcreteObserver("obs2")
        subject.attach(obs1)
        subject.attach(obs2)
        subject.notify("hello")
        self.assertEqual(obs1.received, "hello")
        self.assertEqual(obs2.received, "hello")

    def test_detach(self):
        subject = Subject()
        obs = ConcreteObserver("obs")
        subject.attach(obs)
        subject.detach(obs)
        subject.notify("hello")
        self.assertIsNone(obs.received)


class TestStrategy(unittest.TestCase):
    def test_add(self):
        ctx = Context(AddStrategy())
        self.assertEqual(ctx.execute(3, 4), 7)

    def test_subtract(self):
        ctx = Context(SubtractStrategy())
        self.assertEqual(ctx.execute(10, 3), 7)

    def test_multiply(self):
        ctx = Context(MultiplyStrategy())
        self.assertEqual(ctx.execute(3, 4), 12)

    def test_switch_strategy(self):
        ctx = Context(AddStrategy())
        self.assertEqual(ctx.execute(3, 4), 7)
        ctx.strategy = MultiplyStrategy()
        self.assertEqual(ctx.execute(3, 4), 12)


class TestCommand(unittest.TestCase):
    def test_execute(self):
        invoker = Invoker()
        result = invoker.execute(PrintCommand("hello"))
        self.assertEqual(result, "hello")

    def test_undo(self):
        invoker = Invoker()
        invoker.execute(PrintCommand("hello"))
        result = invoker.undo()
        self.assertEqual(result, "Undo: hello")

    def test_undo_empty(self):
        invoker = Invoker()
        self.assertIsNone(invoker.undo())


class TestTemplateMethod(unittest.TestCase):
    def test_html_report(self):
        report = HTMLReport()
        self.assertEqual(report.generate(), "<html>Some data</html>")

    def test_text_report(self):
        report = TextReport()
        self.assertEqual(report.generate(), "*** Some data ***")


class TestState(unittest.TestCase):
    def test_initial_state(self):
        door = Door()
        self.assertEqual(door.state_name(), "closed")

    def test_open_door(self):
        door = Door()
        door.open()
        self.assertEqual(door.state_name(), "opened")

    def test_close_door(self):
        door = Door()
        door.open()
        door.close()
        self.assertEqual(door.state_name(), "closed")

    def test_double_open(self):
        door = Door()
        door.open()
        door.open()
        self.assertEqual(door.state_name(), "opened")


class TestChainOfResponsibility(unittest.TestCase):
    def test_handled(self):
        h1 = ConcreteHandler(1)
        h2 = ConcreteHandler(2)
        h3 = ConcreteHandler(3)
        h1.set_next(h2).set_next(h3)
        self.assertEqual(h1.handle(2), "Handler 2 handled request 2")

    def test_first_handler(self):
        h1 = ConcreteHandler(1)
        h2 = ConcreteHandler(2)
        h1.set_next(h2)
        self.assertEqual(h1.handle(1), "Handler 1 handled request 1")

    def test_unhandled(self):
        h1 = ConcreteHandler(1)
        h2 = ConcreteHandler(2)
        h1.set_next(h2)
        self.assertIsNone(h1.handle(99))


if __name__ == "__main__":
    unittest.main()
