package model.type;

import model.value.Value;

public interface Type {
    boolean equals(Object another);
    String toString();

    boolean equals(Type anotherType);

    Value defaultValue();

    Type deepCopy();
}
